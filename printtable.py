def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

multtable(1, 4, 7)


def powertable(power, number):
    """
    Print the powertable for <number^power>. 
    Print this output for every <number^power>.
    """

    for i in range(1, number+1):
        print(f"{i} ^{power} = {i**power}")

if __name__ == '__main__':
    powertable(2, 4)
    powertable(3, 3)
        
