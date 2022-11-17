import chiplet_cost_calculator as c

print(f"Interposer cost is ${c.interposer_cost(10):.2f}")
print(f"Assembly time for 10 chiplets is {c.assembly_time(10):.0f}s")
print(f"Assembly cost for 10 chiplets on 10mm^2 interposer is ${c.assembly_cost(10,10):.2f}")
print(f"Assembly cost for 10 chiplets on 800mm^2 interposer is ${c.assembly_cost(10,858):.2f}")
