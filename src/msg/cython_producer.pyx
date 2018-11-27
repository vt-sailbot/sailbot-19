# distutils: sources = producer.c relay.c
# distutils: include_dirs = Python.h
from pickle import Pickler, Unpickler
from cpython.ref cimport PyObject
from libc.string cimport strcpy
from libc.stdlib cimport malloc


cdef extern register_to_produce_data(int channelName, int dataSize)
cdef extern publish_data(int channelName, int dataSize, int *sourcePtr)
cdef extern deregister_to_produce_data(int channelName)



def publish(channelName, dataSize):
    """
    Register with relay to produce data... Relay assigns a pointer to shared memory for it to publish to

    Channel name and data pointer location is stored in hash table by relay, where it can be accessed later by both consumers and producers

    Keyword arguments:
    channel_name -- The name of the channel to publish to (need to coordinate with consumers to have matching values
    data_size -- Size of the data to be passed to relay
    buffer_size -- Used in conjunction with data_size to determine total size of shared memory to be assigned to this channel
    """

    // if search returns Null.... create channel

        register_to_produce_data(channelName, dataSize)

    publish_data(...)

def push_data(channelName, data):
    """
    Push data to shared memory through cython

    Data will be converted to bytearray before pushed to memory

    Keyword arguments:
    channelName -- The name of the channel to publish to
    data -- Data to be published to shared memory
    """

    pickled_data = Pickler(data)

    cython_publish_data(channelName, sizeof(pickled_data), pickled_data) 

def depublish(channelName):

    cython_depublish(channelName)


cdef cython_publish_data(channelName, dataSize, pickled_data):
    
    cdef int C_dataSize = <int>dataSize

    cdef int C_pickled_data = <int> malloc(C_dataSize * sizeof(int))

    for i in range(dataSize):

        C_pickled_data[i] = <int>(pickled_data[i])

    cdef int *sourcePtr = &C_pickled_data

    cdef int C_channelName = <int>channelName

    publish_data(C_channelName, C_dataSize, sourcePtr)


cdef cython_depublish(channelName):

    cdef int C_channelName = <int>channelName

    deregister_to_produce_data(C_channelName)

