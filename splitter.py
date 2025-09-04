import multitasking # type: ignore
from sentiment_analysis import score_paragraph

@multitasking.task  
def score(chunks_data,index):
    out = score_paragraph(chunks_data)
    print("Processing => ",index)
    return out

if __name__ == "__main__":
    with open("huge.txt","r", encoding="utf-8") as f:
        huge_text = f.read()

    chunks = huge_text.split("\n")
    for i,chunk in enumerate(chunks):
            score(chunk,i)
    multitasking.wait_for_tasks()