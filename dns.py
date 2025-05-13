import socket
import struct

def build_dns_query(domain):
    transactio_id = 0x1234
    flags = 0x0100 #standard query with resursion desired
    qdcount  = 1

    #dns header - takes 12 bytes
    header = struct.pack(">HHHHHH", transactio_id, flags, qdcount, 0, 0, 0)

    #QNAME: www.example.com -> 03 'www' 07 'example' 03 'com' 00
    qname = b''.join((bytes([len(label)]) + label.encode() for label in domain.split('.')))
    qname += b'\x00'

    # QTYPE and QCLASS
    qtype = 1 #A record
    qclass = 1 #IN (Internet)

    question = qname + struct.pack(">HH", qtype, qclass)

    return header + question


def send_query(domain, server = "8.8.8.8"):
    query = build_dns_query(domain=domain)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)
    sock.sendto(query, (server, 53))

    try:
        response, _ = sock.recvfrom(512)
        print("Received raw response: ", response.hex())
    except socket.timeout:
        print("No response")
    finally:
        sock.close()

if __name__ == "__main__":
    send_query("example.com")