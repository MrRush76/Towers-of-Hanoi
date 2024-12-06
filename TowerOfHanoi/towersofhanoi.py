def towers_of_hanoi(n, source, target, helper):
  if n == 1:
    print("Move disk 1 from rod", source, "to rod", target)
    return
  towers_of_hanoi(n-1, source,helper,target)

  print("Move disk", n, "from rod", source, "to rod", target)

  towers_of_hanoi(n-1, helper, target, source)

def current_state(n, source, target, helper):
  print("n = ", n, "source = ", source, "target = ", target, "helper = ", helper)
  
n = 3
towers_of_hanoi(n, 'A', 'C', 'B')
