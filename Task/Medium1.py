def tower(n, A, B, C):
    if n > 0:
        tower(n - 1, A, C, B)
        print(f"Disk {n} moved from {A} to {B}")
        tower(n - 1, C, B, A)


numberdisks = 2
tower(numberdisks, 'A', 'C', 'B')
