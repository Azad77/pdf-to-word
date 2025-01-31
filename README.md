# PDF to Word Converter Django App

This is a simple Django web application that allows users to upload a PDF file, convert it to a Word document, and download the converted file. The app utilizes the `pdfplumber` library for extracting text from PDF files and the `python-docx` library for creating Word documents.

## Features
- Upload a PDF file.
- Extracts text from the PDF using `pdfplumber`.
- Converts the extracted text into a Word document (`.docx` format).
- Allows users to download the converted Word document.

## Technologies Used
- **Django** - A high-level Python web framework.
- **pdfplumber** - A Python library for extracting text from PDF files.
- **python-docx** - A Python library for creating and modifying Word documents.

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/pdf-to-word-django.git
cd pdf-to-word-django
```
2. Set Up Virtual Environment
Create a virtual environment and activate it:
```bash
conda create -n pdf_to_word_env python=3.9
conda activate pdf_to_word_env
```
3. Install Dependencies
Install all the required dependencies:

```bash
pip install -r requirements.txt
```
Make sure to include requirements.txt in your repository, containing the necessary libraries:

```text
django==3.2
pdfplumber==0.5.28
python-docx==0.8.11
```
4. Apply Migrations
Run the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
5. Run the Application Locally
Start the development server:

```bash
python manage.py runserver
```
Visit the app in your browser at http://127.0.0.1:8000/ to test the functionality.

## Usage

1. Navigate to the home page of the app.
2. Upload a PDF file that you want to convert.
3. Click the **"Convert"** button.
4. Once the conversion is complete, the Word document will be available for download.

## Deployment

This application can be deployed on platforms such as **Render** or **Railway**. For deployment instructions, please refer to the respective platform's documentation.

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

### Steps for Contributing:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Local Testing

Visit the app in your browser at `http://127.0.0.1:8000/` to test the functionality.

=======
# pdf-to-word
>>>>>>> ba0b12ae6eef55deef18525ac86bcedf12a4d55d
