input = open("11.txt").read().strip().splitlines()

devices = {}
for row in input:
    devices[row[:3]] = row.split(" ")[1:]

def paths(start = "you", goal = "out"):
    memory = {"out": 0}
    memory[goal] = 1

    def helper(device):
        if device not in memory:
            memory[device] = 0
            for output in devices[device]:
                memory[device] += helper(output)
        return memory[device]
    
    return helper(start)

print(paths())
print(max(paths("svr", "fft")*paths("fft", "dac")*paths("dac", "out"), paths("svr", "dac")*paths("dac", "fft")*paths("fft", "out")))