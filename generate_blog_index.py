import csv
from datetime import datetime

TEMPLATE_HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Adam Szava - Blog</title>
    <link rel="stylesheet" href="../style.css">
    <style>
        .tag {
            display: inline-block;
            padding: 0.2em 0.6em;
            margin: 0.2em;
            border-radius: 4px;
            font-size: 0.9em;
            color: white;
        }
        .graph-theory { background-color: #0074D9; }
        .real-analysis { background-color: #2ECC40; }
        .combinatorics { background-color: #FF851B; }
        .number-theory { background-color: #B10DC9; }
        .algebra { background-color: #FF4136; }
    </style>
</head>
<body>
    <header>
        <h1>Blog</h1>
        <p>Proofs, problems, and mathematical curiosities</p>
    </header>
    <nav>
        <a href="../index.html#home">Home</a>
        <a href="index.html">Blog</a>
        <a href="../index.html#projects">Projects</a>
    </nav>
    <main>
"""


TEMPLATE_FOOTER = """
    </main>
    <footer>
        <p>&copy; 2025 Adam Szava. adam.szava@torontomu.ca</p>
    </footer>
</body>
</html>
"""

TAG_COLORS = {
    "Graph Theory": "graph-theory",
    "Real Analysis": "real-analysis",
    "Combinatorics": "combinatorics",
    "Number Theory": "number-theory",
    "Algebra": "algebra"
}

def make_tag_html(tag):
    class_name = TAG_COLORS.get(tag, "tag")
    return f'<span class="tag {class_name}">{tag}</span>'

def generate_blog_index(csv_path, output_path):
    posts_html = ""
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row["title"]
            filename = row["filename"]
            date = row["date"]
            tags = [tag.strip() for tag in row["tags"].split(",")]
            summary = row["summary"]
            tags_html = " ".join(make_tag_html(tag) for tag in tags)
            post_html = f"""
            <article>
                <h3><a href="{filename}">{title}</a></h3>
                <div>{tags_html}</div>
                <p><em>{date}</em></p>
                <p>{summary}</p>
            </article>
            """
            posts_html += post_html

    full_html = TEMPLATE_HEADER + posts_html + TEMPLATE_FOOTER
    with open(output_path, "w") as f:
        f.write(full_html)

# Example usage:
generate_blog_index("blog/posts.csv", "blog/index.html")
