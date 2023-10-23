from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import io
from pypdf import PdfReader
import io
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter

def landing_redirect(request):
    return HttpResponseRedirect(reverse('dashboard:home'))

def dashboard(request):
    return render(request, 'dashboard.html')

def upload_pdf(request):
    if request.POST and request.FILES['pdf_file']:
        nlp = spacy.load("en_core_web_sm")

        pdf_file = request.FILES['pdf_file'].read()

        pdf_reader = PdfReader(io.BytesIO(pdf_file))

        num_pages = len(pdf_reader.pages)
        i = 0
        content = []

        text = pdf_reader.pages[1]            
        doc = nlp(text.extract_text())

        # Exclude stopwords... What ever that means?
        sentences = [sent for sent in doc.sents if sent.text not in STOP_WORDS]

        # Calculate the term frequency of words
        word_freq = Counter()
        for token in doc:
            word_freq[token.text] += 1

        # Calculate the sentence score based on term frequency
        sentence_scores = {}
        for sentence in sentences:
            for word in sentence:
                if word.text in word_freq:
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word.text]

        # Sort sentences by score and get the top N sentences for summary
        summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:5]
        summary = ' '.join([sent.text for sent in summary_sentences])
        print(summary)
        return render(request, 'upload_pdf.html', {'content': summary})
    else:
        return render(request, 'upload_pdf.html')