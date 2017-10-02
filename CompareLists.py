def compareLists(arr1, arr2):
    if arr1 == arr2:
        print "The lists are the same"
    else:
        print "The lists are not the same"

compareLists([1,2,5,6,2], [1,2,5,6,2])
compareLists([1,2,5,6,5], [1,2,5,6,5,3])
compareLists([1,2,5,6,5,16], [1,2,5,6,5])
compareLists(['celery','carrots','bread','milk'], ['celery','carrots','bread','cream'])