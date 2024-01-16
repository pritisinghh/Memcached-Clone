# Memcached-lite Server

## Introduction

This repository contains the implementation of a simplified version of a Memcached server, referred to as Memcached-lite. The server is designed to store and retrieve data for different clients using the set and get commands.

## Server Methods

### Set

The set command is whitespace delimited and consists of two lines:
```
set <key> <value-size-bytes> \r\n
<value> \r\n
```
Note: This simplified version does not include flags and expiry time parameters, which are part of the complete Memcached protocol.

The server responds with either "STORED\r\n" if the operation is successful, or "NOT-STORED\r\n" if there is an issue.

### Get

Retrieving data is done using the following command:
```
get <key>\r\n
```
The server responds with two lines:
```
VALUE <key> <bytes> \r\n
<data block>\r\n
```
After transmitting all items, the server sends the string "END\r\n".

## How to Run

1. Run the Memcached-lite server using the provided script or command.
2. Clients can connect to the server and send set or get commands to store or retrieve data.

## Code Structure

- `memcached_lite.py`: Main server implementation.
- `client.py`: Sample client script to interact with the server.
- `config.py`: Configuration file specifying server parameters.

# How to run 

## Server

`
python server.py
`

## Client 

`
python client.py
`
