


from collections import Counter


def find_most_frquent_ips(ips):
    ips = list(ips)
    list_ips = []
    for i in ips:
        list_ips.append(i.split(" ")[0])
    counter = Counter(list_ips)
    print(counter)
    return [k for k, v in counter.items() if v == max(counter.values())]


ips = {
    "10.0.0.1 - GET 2020-08-24", 
    "10.0.0.1 - GET 2020-08-25",
    "10.0.0.1 - GET 2020-08-23", 
    "10.0.0.2 - GET 2020-08-22", 
    "10.0.0.3 - GET 2020-08-21", 
    "10.0.0.3 - GET 2020-08-20",
    "10.0.0.3 - GET 2020-08-19",
    "10.0.0.4 - GET 2020-08-18"
}


print("Max: ", find_most_frquent_ips(ips))