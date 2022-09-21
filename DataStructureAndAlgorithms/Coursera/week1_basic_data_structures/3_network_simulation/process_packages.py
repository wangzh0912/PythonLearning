# python3

from collections import namedtuple, deque

Request = namedtuple('Request', ['arrived_at', 'time_to_process'])


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    # start_times stores the start time of each packet
    start_times = [None] * len(requests)

    # the buffer stores the finish time of each packet
    finish_times = deque(maxlen=buffer_size)

    for i, (arrived_at, time_to_process) in enumerate(requests):

        # pop left all the packets that have been processed
        while finish_times and finish_times[0] <= arrived_at:
            finish_times.popleft()

        # check if the buffer is full, if full, drop the new packet
        if len(finish_times) >= buffer_size:
            start_times[i] = -1
        else:
            # check the finish time of latest packet in the buffer
            if finish_times:
                latest_time = finish_times[-1]
            else:
                latest_time = 0
            # the start time of processing the new packet is the maximum time of 
            # the finishing time of the latest packet in the buffer
            # and the arrival time of the new packet
            start_times[i] = max(latest_time, arrived_at)
            finish_times.append(start_times[i] + time_to_process)

    for start_time in start_times:
        print(start_time)

 


if __name__ == "__main__":
    main()
