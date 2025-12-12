input = open("11.txt").read().strip().splitlines()

devices = {}
for row in input:
    devices[row[:3]] = row.split(" ")[1:]

def paths(start = "you", goal = "out"):
    memory = {goal: 1}
    if goal != "out": memory["out"] = 0

    def helper(device):
        if device in memory:
            return memory[device]
        memory[device] = 0
        for output in devices[device]:
            memory[device] += helper(output)
        return memory[device]
    
    return helper(start)

print(paths("you", "out"))
print(max(paths("svr", "fft")*paths("fft", "dac")*paths("dac", "out"), paths("svr", "dac")*paths("dac", "fft")*paths("fft", "out")))