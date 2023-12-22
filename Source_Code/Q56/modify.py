import json

params = [24,
56,
93,
41,
64,
23,
117,
30,
34,
55,
78,
47,
53,
85,
3,
124,
37,
63,
18,
50,
106,
22,
42,
52,
67,
33,
57,
44,
95,
79,
46,
71,
105,
84,
27,
146,
65,
35,
94,
2,
74,
45,
86,
90,
29,
87,
91,
120,
73,
11,
96,
15,
25,
28,
40,
69,
60,
127,
77,
36,
39,
32,
19,
8,
81,
26,
43,
75,
99,
12,
17,
88,
20,
97,
16,
149,
144,
49,
61,
31,
98,
100,
48,
114,
14,
143,
58,
68,
38,
130,
6,
9,
54,
70,
89,
21,
142,
10,
110,
92]

for i in range(3,5):
    for j in range(1,101):
        with open(f"command_results_{i}/Folder_{j}/response.txt", "r") as f:
            lines = f.readlines()
            updated_lines = []

        for line in lines:
            if "permutations" in line and params[j-1] > 9:
                updated_line = line.replace("permutations(s)", "permutations('')")
                updated_lines.append(updated_line)
            else:
    
                updated_lines.append(line)

        with open(f"command_results_{i}/Folder_{j}/response.txt", 'w') as file:
            file.writelines(updated_lines)
               



