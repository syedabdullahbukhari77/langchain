from langchain_core.document import Document

doc = Document(
    page_content='hey these are the words for langchain to describe the area | work;',
    metadata={
        'source' : 'example.txt',
        'pages' : 1,
        'author' : 'abdullah syed',
        'date_created' : '2025-10-25'
    }
)
