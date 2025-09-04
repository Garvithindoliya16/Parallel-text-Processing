import multitasking #type:ignore
import time
@multitasking.task

def fetch_data(url_id):
    time.sleep(1)
    return f"Data from {url_id}"


for i in range(5):
    fetch_data(i)



multitasking.wait_for_tasks()
print("All data fetched!")


