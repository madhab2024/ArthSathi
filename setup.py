from setuptools import setup, find_packages

setup(
    name="financial_sentiment",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn==0.24.0",
        "streamlit==1.28.2",
        "pandas==2.1.3",
        "numpy==1.26.2",
        "scikit-learn==1.3.2",
        "transformers==4.35.2",
        "torch==2.2.0",
        "beautifulsoup4==4.12.2",
        "selenium==4.15.2",
        "requests==2.31.0",
        "nltk==3.8.1",
        "spacy==3.7.2",
        "plotly==5.18.0",
        "python-multipart==0.0.6",
        "pydantic==2.5.2",
    ],
) 