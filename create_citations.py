import xml.etree.ElementTree as ET

# List of all citations with details
citations = [
    {
        "tag": "Source1",
        "author": "Mayo Clinic",
        "title": "Domestic violence against women: Recognize patterns, seek help",
        "year": "n.d.",
        "url": "https://www.mayoclinic.org",
    },
    {
        "tag": "Source2",
        "author": "Corry, C. E., Fiebert, M. S., & Pizzey, E.",
        "title": "Controlling domestic violence against men",
        "year": "2002",
        "url": "https://citeseerx.ist.psu.edu",
    },
    {
        "tag": "Source3",
        "author": "Government of the Netherlands",
        "title": "What is domestic violence?",
        "year": "n.d.",
        "url": "https://www.government.nl",
    },
    {
        "tag": "Source4",
        "author": "The Advocates for Human Rights",
        "title": "The Advocates for Human Rights",
        "year": "2015",
        "url": "https://upr-inf.org",
    },
    {
        "tag": "Source5",
        "author": "Giving Compass",
        "title": "Changing the domestic violence abuse narrative for good",
        "year": "n.d.",
        "url": "https://www.givingcompass.org",
    },
    {
        "tag": "Source6",
        "author": "Medium",
        "title": "People can’t believe domestic violence is a human rights issue",
        "year": "2019",
        "url": "https://www.medium.com",
    },
    {
        "tag": "Source7",
        "author": "Deshpande, S.",
        "title": "Socio-cultural and legal aspects of violence against men",
        "year": "2019",
        "url": "https://journals.sagepub.com",
    },
    {
        "tag": "Source8",
        "author": "CDC",
        "title": "Intimate partner violence, sexual violence and stalking among men",
        "year": "n.d.",
        "url": "https://www.cdc.gov",
    },
    {
        "tag": "Source9",
        "author": "Robinson, L., & Segal, J.",
        "title": "Help for men who are being abused",
        "year": "2021",
        "url": "https://www.helpguide.org",
    },
    {
        "tag": "Source10",
        "author": "Kolbe, V., & Buttner, A.",
        "title": "Domestic Violence against Men-prevalence and Risk Factor",
        "year": "2020",
        "url": "https://www.ncbi.nlm.nih.gov",
    },
    {
        "tag": "Source11",
        "author": "BBC",
        "title": "Male domestic abuse victims 'sleeping in cars and tents'",
        "year": "2020",
        "url": "https://www.bbc.com",
    },
    {
        "tag": "Source12",
        "author": "Ghimire, C., Acharya, S., Shrestha, C., K.C, P., Singh, S., & Sharma, P.",
        "title": "Interpersonal Violence During the COVID-19 Lockdown Period in Nepal: A Descriptive Cross-Sectional Study",
        "year": "2020",
        "url": "https://jnma.com.np",
    },
    {
        "tag": "Source13",
        "author": "Stop Abuse for Everyone",
        "title": "Celebrity Domestic Violence Case",
        "year": "2020",
        "url": "https://www.stopabuseforeveryone.org",
    },
    {
        "tag": "Source14",
        "author": "Pfeifer, H.",
        "title": "Men as victims of domestic violence: 'I was paralyzed'",
        "year": "2020",
        "url": "https://www.dw.com",
    },
    {
        "tag": "Source15",
        "author": "Rees, J.",
        "title": "Male domestic abuse victims 'suffering in silence'",
        "year": "2019",
        "url": "https://www.bbc.com",
    },
    {
        "tag": "Source16",
        "author": "The Advocates for Human Rights",
        "title": "Domestic Violence in Nepal",
        "year": "1998",
        "url": "https://www.theadvocatesforhumanrights.org",
    },
    {
        "tag": "Source17",
        "author": "Shrestha, D., & Bhandari, N.",
        "title": "Battered Women Syndrome: Need for Judicial Objectivity",
        "year": "2018",
        "url": "https://nepjol.info",
    },
    {
        "tag": "Source18",
        "author": "The Himalayan Times",
        "title": "Violence against Men up in Kavre",
        "year": "2015",
        "url": "https://www.thehimalayantimes.com",
    },
]

# Create the root element
root = ET.Element(
    "Sources",
    xmlns="http://schemas.openxmlformats.org/officeDocument/2006/bibliography",
)

# Populate the XML tree with sources
for citation in citations:
    source = ET.SubElement(root, "Source")
    ET.SubElement(source, "Tag").text = citation["tag"]
    ET.SubElement(source, "SourceType").text = (
        "Book"  # Word requires a SourceType, here we use 'Book' as a general type
    )
    ET.SubElement(source, "Author").text = citation["author"]
    ET.SubElement(source, "Title").text = citation["title"]
    ET.SubElement(source, "Year").text = citation["year"]
    ET.SubElement(source, "URL").text = citation["url"]
    ET.SubElement(source, "RefOrder").text = str(citations.index(citation) + 1)

# Create the XML tree and write to a file
tree = ET.ElementTree(root)
tree.write("MyCitations.xml", encoding="utf-8", xml_declaration=True)

print("XML file 'MyCitations.xml' created successfully.")
