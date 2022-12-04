# python3
#%%
from collections import namedtuple
import heapq 

AssignedJob = namedtuple('AssignedJob', ['worker', 'started_at'])

class Worker():
    """The workers are sorted by release time. 
    If the release time is the same, workers are sorted by their thread_id.
    """
    def __init__(self, thread_id: int, release_time: int = 0) -> None:
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time


class ParallelQueue():
    
    def __init__(self, n_workers: int, jobs: list) -> None:
        self.n_workers = n_workers
        self.jobs = jobs
    
    def assign_jobs(self) -> list:
        """Use priority queue to assign jobs for workers.
        The priority is the release time for each workers (defined in the Worket class).
        1. Pop out the worker which has the lowest release time.
        2. Assign this worker the current job.
        3. Push back the worker to the priority queue.

        Returns:
            list: The result that stores namedtuple AssignedJob
        """
        self.result = [None] * len(self.jobs)
        self.priority_queue = [Worker(i) for i in range(self.n_workers)]

        for i, job in enumerate(self.jobs):
            curr_free_worker = heapq.heappop(self.priority_queue)
            self.result[i] = AssignedJob(curr_free_worker.thread_id, curr_free_worker.release_time)
            curr_free_worker.release_time += job
            heapq.heappush(self.priority_queue, curr_free_worker)
        return self.result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    parallel_queue = ParallelQueue(n_workers, jobs)
    assigned_jobs = parallel_queue.assign_jobs()

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()



# %%
