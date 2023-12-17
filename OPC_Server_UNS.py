import sys

sys.path.insert(0, "..")
import time

from opcua import ua, Server, uamethod


@uamethod
def multiply(x, y):
    print("Multiply was called with args " + x + " & " + y)
    # result.set_value(x * y)
    return x * y


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 0.0)
    result = myobj.add_variable(idx, "Result", 0)
    result.set_writable()
    myvar.set_writable()  # Set MyVariable to be writable by clients

    inargx = ua.Argument()
    inargx.Name = "x"
    inargx.DataType = ua.NodeId(ua.ObjectIds.Int64)
    inargx.ValueRank = -1
    inargx.ArrayDimensions = []
    inargx.Description = ua.LocalizedText("First number x")
    inargy = ua.Argument()
    inargy.Name = "y"
    inargy.DataType = ua.NodeId(ua.ObjectIds.Int64)
    inargy.ValueRank = -1
    inargy.ArrayDimensions = []
    inargy.Description = ua.LocalizedText("Second number y")
    outarg = ua.Argument()
    outarg.Name = "Result"
    outarg.DataType = ua.NodeId(ua.ObjectIds.Int64)
    outarg.ValueRank = -1
    outarg.ArrayDimensions = []
    outarg.Description = ua.LocalizedText("Multiplication result")

    myobj.add_method(idx, "multiply", multiply, [inargx, inargy], [outarg])
    # starting!
    server.start()

    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(count)
    finally:
        # close connection, remove subscriptions, etc
        server.stop()
