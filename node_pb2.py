# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nnode.proto\"\x07\n\x05\x45mpty\"!\n\x0eTimeoutMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"J\n\x11TimeoutSetRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x14\n\x0ctime_seconds\x18\x02 \x01(\x05\x12\x0f\n\x07node_id\x18\x03 \x01(\x05\"\x1e\n\nInitParams\x12\x10\n\x08list_ids\x18\x01 \x03(\x05\":\n\x10\x45lectionResponse\x12\x11\n\tleader_id\x18\x01 \x01(\x05\x12\x13\n\x0bleader_time\x18\x02 \x01(\t\"\x1d\n\x08LeaderID\x12\x11\n\tleader_id\x18\x01 \x01(\x05\"%\n\x0fSuccessResponse\x12\x12\n\nisComplete\x18\x01 \x01(\x08\"G\n\x06Symbol\x12\x0b\n\x03pos\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07node_id\x18\x03 \x01(\x05\x12\x11\n\tnode_time\x18\x04 \x01(\t\"h\n\x0eSymbolResponse\x12\x12\n\nisComplete\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x1d\n\x05\x62oard\x18\x05 \x01(\x0b\x32\x0e.BoardResponse\x12\x12\n\nisFinished\x18\x06 \x01(\x08\"2\n\rBoardResponse\x12\r\n\x05\x62oard\x18\x01 \x01(\t\x12\x12\n\nisComplete\x18\x02 \x01(\x08\".\n\x08NodeTime\x12\x11\n\tnode_time\x18\x01 \x01(\t\x12\x0f\n\x07node_id\x18\x02 \x01(\x05\"&\n\x08TimeDiff\x12\x1a\n\x12total_time_seconds\x18\x01 \x01(\x01\"\x1b\n\x06Leader\x12\x11\n\twinner_id\x18\x01 \x01(\x05\"$\n\x0eLeaderResponse\x12\x12\n\nisComplete\x18\x02 \x01(\x08\"\x1e\n\x07TimeOut\x12\x13\n\x0bset_timeout\x18\x01 \x01(\x05\"%\n\x0fTimeoutResponse\x12\x12\n\nisComplete\x18\x01 \x01(\x08\"\x18\n\x06Winner\x12\x0e\n\x06winner\x18\x01 \x01(\t2\x9e\x03\n\tTicTacToe\x12+\n\tStartGame\x12\x0b.InitParams\x1a\x11.ElectionResponse\x12+\n\x0cNotifyLeader\x12\t.LeaderID\x1a\x10.SuccessResponse\x12%\n\tSetSymbol\x12\x07.Symbol\x1a\x0f.SymbolResponse\x12#\n\tListBoard\x12\x06.Empty\x1a\x0e.BoardResponse\x12%\n\tSetLeader\x12\x07.Leader\x1a\x0f.LeaderResponse\x12 \n\x0bRequestTime\x12\x06.Empty\x1a\t.NodeTime\x12 \n\x0bSetTimeDiff\x12\t.TimeDiff\x1a\x06.Empty\x12\x1f\n\x0cNotifyWinner\x12\x07.Winner\x1a\x06.Empty\x12(\n\rNotifyTimeout\x12\x0f.TimeoutMessage\x1a\x06.Empty\x12\x35\n\x0eSetTimeoutTime\x12\x12.TimeoutSetRequest\x1a\x0f.TimeoutMessageb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'node_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=14
  _EMPTY._serialized_end=21
  _TIMEOUTMESSAGE._serialized_start=23
  _TIMEOUTMESSAGE._serialized_end=56
  _TIMEOUTSETREQUEST._serialized_start=58
  _TIMEOUTSETREQUEST._serialized_end=132
  _INITPARAMS._serialized_start=134
  _INITPARAMS._serialized_end=164
  _ELECTIONRESPONSE._serialized_start=166
  _ELECTIONRESPONSE._serialized_end=224
  _LEADERID._serialized_start=226
  _LEADERID._serialized_end=255
  _SUCCESSRESPONSE._serialized_start=257
  _SUCCESSRESPONSE._serialized_end=294
  _SYMBOL._serialized_start=296
  _SYMBOL._serialized_end=367
  _SYMBOLRESPONSE._serialized_start=369
  _SYMBOLRESPONSE._serialized_end=473
  _BOARDRESPONSE._serialized_start=475
  _BOARDRESPONSE._serialized_end=525
  _NODETIME._serialized_start=527
  _NODETIME._serialized_end=573
  _TIMEDIFF._serialized_start=575
  _TIMEDIFF._serialized_end=613
  _LEADER._serialized_start=615
  _LEADER._serialized_end=642
  _LEADERRESPONSE._serialized_start=644
  _LEADERRESPONSE._serialized_end=680
  _TIMEOUT._serialized_start=682
  _TIMEOUT._serialized_end=712
  _TIMEOUTRESPONSE._serialized_start=714
  _TIMEOUTRESPONSE._serialized_end=751
  _WINNER._serialized_start=753
  _WINNER._serialized_end=777
  _TICTACTOE._serialized_start=780
  _TICTACTOE._serialized_end=1194
# @@protoc_insertion_point(module_scope)
