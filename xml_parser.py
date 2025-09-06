# parse_100_books.py
import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse("bookstore_500.xml")
root = tree.getroot()

books = []
for book in root.findall("book"):
    category = book.get("category")
    title_elem = book.find("title")
    title = title_elem.text if title_elem is not None else ""
    lang = title_elem.get("lang") if title_elem is not None else ""
    author = book.findtext("author", default="")
    price = float(book.findtext("price", default="0") or 0)
    books.append({
        "category": category,
        "title": title,
        "lang": lang,
        "author": author,
        "price": price
    })

df = pd.DataFrame(books)

# show first 200 rows

for i, row in df.head(200).iterrows():
    print(f"{i}: {row['category']} | {row['title']} | {row['lang']} | {row['author']} | {row['price']}")


df.to_csv("books_500.csv", index=False)
df.to_json("books_500.json", orient="records", indent=2)

print(f"\nSaved {len(df)} records to books_500.csv and books_500.json")
