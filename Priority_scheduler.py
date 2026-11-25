import heapq

class PriorityScheduler:
    def __init__(self):
        self.queue = []
        self.job_counter = 0

    def add_job(self, job_name, priority):
        heapq.heappush(self.queue, (-priority, self.job_counter, job_name))
        self.job_counter += 1

    def release_next(self):
        if not self.queue:
            return None
        return heapq.heappop(self.queue)[2]

print("\n Activity 6 ")
scheduler = PriorityScheduler()
scheduler.add_job("Low Priority Task", 1)
scheduler.add_job("Critical Bug Fix", 10)
scheduler.add_job("Medium Task", 5)
scheduler.add_job("High Priority Task", 8)

release_order = []
while scheduler.queue:
    release_order.append(scheduler.release_next())

print("Release order:", release_order)
