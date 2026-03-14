# IIITBBSR_Hackathon
This folder contains all works of iit hackathon.

<h1>CLARKE ENGINE — Upside Down Archive</h1>
<h2>📁 Project Overview</h2>
An interactive web experience inspired by Stranger Things' "Upside Down" aesthetic. Features a dual-layer image reveal with torch effect, scroll-triggered document scanner, and vintage CRT styling.

<h1>Project Directive 3: Mr. Clarke's Automated Briefing Generator</h1>
Based on the provided documents, Project 3 (codenamed "Mr. Clarke's Automated Briefing
Generator") is an AI-powered system designed to process complex research data and transform
it into visual presentations.

<h2>Project Summary</h2>
The objective is to build an engine that can ingest a folder containing text or PDF documents—
specifically themed around Mr. Clarke's physics notes and research on the "Upside Down"—and
automatically generate a fully formatted, animated presentation deck. Unlike a standard chatbot,
this system must programmatically create the actual slide files (such as .pptx or HTML5 slides).

<h2>Core Requirements include:</h2>
<ul>
<li>Document Ingestion: Processing local folders of reference materials.</li>
<li>Automated Output: Generating multi-slide decks with bullet points and accurate data.</li>
<li>Programmatic Animations: Including automated transitions and sequential element</li>
<li>animations (e.g., fading in bullet points).</li>
<li>Source Citation: Automatically creating a final "References" slide citing specific pages from
the source documents.</li>
</ul>


<h2>Architectural Flow</h2>
<ol>
The engine follows a structured pipeline to move from raw data to a finished presentation:
<li>Data Ingestion & Chunking: The system reads the local PDF/text documents and "intelligently
chunks" the data into manageable pieces for the AI to process.</li>
<li>Information Retrieval (RAG): Using Retrieval-Augmented Generation, the engine identifies and
extracts the most relevant information from the chunks based on a user’s prompt or question.</li>
<li>Logical Structuring: The AI outlines a logical presentation structure, deciding how many slides
are needed and what content belongs on each.</li>
<li>Content & Asset Generation: The system populates slides with text and can optionally use AI
to generate relevant charts, graphs, or image placeholders.</li>

  </ol>
5. Programmatic Export: Finally, the engine uses an API (like the Google Slides API or a
PowerPoint library) to physically build the file, applying the 80s-themed formatting and
sequential animations.
