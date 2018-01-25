def custom_zip(rdd1, rdd2):
    """
    Custom zipping function for RDDs
    The native PySpark zip() function sssumes that the two RDDs have the same number of partitions and the same number
    of elements in each partition.  This zipper works without that assumption

    The results should be identical to calling rdd1.zip(rdd2)

    :param rdd1: the first rdd to zip
    :param rdd2: the second rdd to zip
    :return: a new rdd with key-value pairs where the keys are elements of the first rdd and values are
            elements of the second rdd
    """

    # create keys for join
    indexed_1 = rdd1.zipWithIndex().map(lambda x: (x[1], x[0]))
    indexed_2 = rdd2.zipWithIndex().map(lambda x: (x[1], x[0]))

    rdd_joined = indexed_1.join(indexed_2).map(lambda x: x[1])

    return rdd_joined