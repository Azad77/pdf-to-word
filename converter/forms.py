"""
Author: Dr. Azad Rasul
Affiliation: Soran University
Email: azad.rasul@soran.edu.iq
Year: 2025
"""

from django import forms

class UploadPDFForm(forms.Form):
    pdf_file = forms.FileField(label="Select a PDF File")
