# Applied Machine Learning (Cornell CS5785, Fall 2024)

This repo contains executable course notes and slides for the Applied ML course at Cornell and Cornell Tech (Fall 2024 edition).

Note that these notes are slightly different from the ones used in my Youtube [lecture videos](https://www.youtube.com/watch?v=vcE9WGbi4QY&list=PL2UML_KCiC0UlY7iCQDSiGDMovaupqc83) videos from the Fall 2020 edition of the course. You may find these in my other Github repo.

## Contents

This repo is organized as follows.

```
.
├── README.md
├── slides.               # Course slides
├── lecture-notes         # Lecture notes (expanding on the material in the slides)
└── requirements.txt      # Packages needed for your virtualenv
```

## Setup

There are packages that you need in your system and in your virtual environment to run the code in this repo.

System packages include Pandoc and Tex Live.
For example, in Ubuntu, you can install them using:

```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic
```

You also need to create a virtual environment with Python.
Packages needed are provided in the `environment.yml` file.
You can follow these instructions to create the virtual environment:

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda.

1. Install main Python environment (allows to run most steps):

   ```bash
   conda env create --name course-cornell-cs5785 --file environment.yml
   ```

1. Activate the environment:

    ```bash
    conda activate course-cornell-cs5785
    ```

## Feedback

Please send feedback to [Volodymyr Kuleshov](https://www.cs.cornell.edu/~kuleshov/)
