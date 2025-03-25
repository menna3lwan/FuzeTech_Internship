from typing import List

def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    extra_satisfied = 0
    max_extra = 0
    always_satisfied = 0

    for i in range(len(customers)):
        if grumpy[i] == 0:
            always_satisfied += customers[i]
        else:
            extra_satisfied += customers[i]

        if i >= minutes and grumpy[i - minutes] == 1:
            extra_satisfied -= customers[i - minutes]

        max_extra = max(max_extra, extra_satisfied)

    return always_satisfied + max_extra

