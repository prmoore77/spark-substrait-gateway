# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/base.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from spark.connect import commands_pb2 as spark_dot_connect_dot_commands__pb2
from spark.connect import common_pb2 as spark_dot_connect_dot_common__pb2
from spark.connect import expressions_pb2 as spark_dot_connect_dot_expressions__pb2
from spark.connect import relations_pb2 as spark_dot_connect_dot_relations__pb2
from spark.connect import types_pb2 as spark_dot_connect_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18spark/connect/base.proto\x12\rspark.connect\x1a\x19google/protobuf/any.proto\x1a\x1cspark/connect/commands.proto\x1a\x1aspark/connect/common.proto\x1a\x1fspark/connect/expressions.proto\x1a\x1dspark/connect/relations.proto\x1a\x19spark/connect/types.proto\"e\n\x04Plan\x12\'\n\x04root\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationH\x00\x12)\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\x16.spark.connect.CommandH\x00\x42\t\n\x07op_type\"\\\n\x0bUserContext\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12)\n\nextensions\x18\xe7\x07 \x03(\x0b\x32\x14.google.protobuf.Any\"\xa1\x10\n\x12\x41nalyzePlanRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x30\n\x0cuser_context\x18\x02 \x01(\x0b\x32\x1a.spark.connect.UserContext\x12\x18\n\x0b\x63lient_type\x18\x03 \x01(\tH\x01\x88\x01\x01\x12:\n\x06schema\x18\x04 \x01(\x0b\x32(.spark.connect.AnalyzePlanRequest.SchemaH\x00\x12<\n\x07\x65xplain\x18\x05 \x01(\x0b\x32).spark.connect.AnalyzePlanRequest.ExplainH\x00\x12\x43\n\x0btree_string\x18\x06 \x01(\x0b\x32,.spark.connect.AnalyzePlanRequest.TreeStringH\x00\x12=\n\x08is_local\x18\x07 \x01(\x0b\x32).spark.connect.AnalyzePlanRequest.IsLocalH\x00\x12\x45\n\x0cis_streaming\x18\x08 \x01(\x0b\x32-.spark.connect.AnalyzePlanRequest.IsStreamingH\x00\x12\x43\n\x0binput_files\x18\t \x01(\x0b\x32,.spark.connect.AnalyzePlanRequest.InputFilesH\x00\x12G\n\rspark_version\x18\n \x01(\x0b\x32..spark.connect.AnalyzePlanRequest.SparkVersionH\x00\x12?\n\tddl_parse\x18\x0b \x01(\x0b\x32*.spark.connect.AnalyzePlanRequest.DDLParseH\x00\x12I\n\x0esame_semantics\x18\x0c \x01(\x0b\x32/.spark.connect.AnalyzePlanRequest.SameSemanticsH\x00\x12G\n\rsemantic_hash\x18\r \x01(\x0b\x32..spark.connect.AnalyzePlanRequest.SemanticHashH\x00\x12<\n\x07persist\x18\x0e \x01(\x0b\x32).spark.connect.AnalyzePlanRequest.PersistH\x00\x12@\n\tunpersist\x18\x0f \x01(\x0b\x32+.spark.connect.AnalyzePlanRequest.UnpersistH\x00\x12N\n\x11get_storage_level\x18\x10 \x01(\x0b\x32\x31.spark.connect.AnalyzePlanRequest.GetStorageLevelH\x00\x1a+\n\x06Schema\x12!\n\x04plan\x18\x01 \x01(\x0b\x32\x13.spark.connect.Plan\x1a\xa8\x02\n\x07\x45xplain\x12!\n\x04plan\x18\x01 \x01(\x0b\x32\x13.spark.connect.Plan\x12K\n\x0c\x65xplain_mode\x18\x02 \x01(\x0e\x32\x35.spark.connect.AnalyzePlanRequest.Explain.ExplainMode\"\xac\x01\n\x0b\x45xplainMode\x12\x1c\n\x18\x45XPLAIN_MODE_UNSPECIFIED\x10\x00\x12\x17\n\x13\x45XPLAIN_MODE_SIMPLE\x10\x01\x12\x19\n\x15\x45XPLAIN_MODE_EXTENDED\x10\x02\x12\x18\n\x14\x45XPLAIN_MODE_CODEGEN\x10\x03\x12\x15\n\x11\x45XPLAIN_MODE_COST\x10\x04\x12\x1a\n\x16\x45XPLAIN_MODE_FORMATTED\x10\x05\x1aM\n\nTreeString\x12!\n\x04plan\x18\x01 \x01(\x0b\x32\x13.spark.connect.Plan\x12\x12\n\x05level\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_level\x1a,\n\x07IsLocal\x12!\n\x04plan\x18\x01 \x01(\x0b\x32\x13.spark.connect.Plan\x1a\x30\n\x0bIsStreaming\x12!\n\x04plan\x18\x01 \x01(\x0b\x32\x13.spark.connect.Plan\x1a/\n\nInputFiles\x12!\n\x04plan\x18\x01 \x01(\x0b\x32\x13.spark.connect.Plan\x1a\x0e\n\x0cSparkVersion\x1a\x1e\n\x08\x44\x44LParse\x12\x12\n\nddl_string\x18\x01 \x01(\t\x1a\x62\n\rSameSemantics\x12(\n\x0btarget_plan\x18\x01 \x01(\x0b\x32\x13.spark.connect.Plan\x12\'\n\nother_plan\x18\x02 \x01(\x0b\x32\x13.spark.connect.Plan\x1a\x31\n\x0cSemanticHash\x12!\n\x04plan\x18\x01 \x01(\x0b\x32\x13.spark.connect.Plan\x1a\x7f\n\x07Persist\x12)\n\x08relation\x18\x01 \x01(\x0b\x32\x17.spark.connect.Relation\x12\x37\n\rstorage_level\x18\x02 \x01(\x0b\x32\x1b.spark.connect.StorageLevelH\x00\x88\x01\x01\x42\x10\n\x0e_storage_level\x1aZ\n\tUnpersist\x12)\n\x08relation\x18\x01 \x01(\x0b\x32\x17.spark.connect.Relation\x12\x15\n\x08\x62locking\x18\x02 \x01(\x08H\x00\x88\x01\x01\x42\x0b\n\t_blocking\x1a<\n\x0fGetStorageLevel\x12)\n\x08relation\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationB\t\n\x07\x61nalyzeB\x0e\n\x0c_client_type\"\x86\x0b\n\x13\x41nalyzePlanResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12;\n\x06schema\x18\x02 \x01(\x0b\x32).spark.connect.AnalyzePlanResponse.SchemaH\x00\x12=\n\x07\x65xplain\x18\x03 \x01(\x0b\x32*.spark.connect.AnalyzePlanResponse.ExplainH\x00\x12\x44\n\x0btree_string\x18\x04 \x01(\x0b\x32-.spark.connect.AnalyzePlanResponse.TreeStringH\x00\x12>\n\x08is_local\x18\x05 \x01(\x0b\x32*.spark.connect.AnalyzePlanResponse.IsLocalH\x00\x12\x46\n\x0cis_streaming\x18\x06 \x01(\x0b\x32..spark.connect.AnalyzePlanResponse.IsStreamingH\x00\x12\x44\n\x0binput_files\x18\x07 \x01(\x0b\x32-.spark.connect.AnalyzePlanResponse.InputFilesH\x00\x12H\n\rspark_version\x18\x08 \x01(\x0b\x32/.spark.connect.AnalyzePlanResponse.SparkVersionH\x00\x12@\n\tddl_parse\x18\t \x01(\x0b\x32+.spark.connect.AnalyzePlanResponse.DDLParseH\x00\x12J\n\x0esame_semantics\x18\n \x01(\x0b\x32\x30.spark.connect.AnalyzePlanResponse.SameSemanticsH\x00\x12H\n\rsemantic_hash\x18\x0b \x01(\x0b\x32/.spark.connect.AnalyzePlanResponse.SemanticHashH\x00\x12=\n\x07persist\x18\x0c \x01(\x0b\x32*.spark.connect.AnalyzePlanResponse.PersistH\x00\x12\x41\n\tunpersist\x18\r \x01(\x0b\x32,.spark.connect.AnalyzePlanResponse.UnpersistH\x00\x12O\n\x11get_storage_level\x18\x0e \x01(\x0b\x32\x32.spark.connect.AnalyzePlanResponse.GetStorageLevelH\x00\x1a\x31\n\x06Schema\x12\'\n\x06schema\x18\x01 \x01(\x0b\x32\x17.spark.connect.DataType\x1a!\n\x07\x45xplain\x12\x16\n\x0e\x65xplain_string\x18\x01 \x01(\t\x1a!\n\nTreeString\x12\x13\n\x0btree_string\x18\x01 \x01(\t\x1a\x1b\n\x07IsLocal\x12\x10\n\x08is_local\x18\x01 \x01(\x08\x1a#\n\x0bIsStreaming\x12\x14\n\x0cis_streaming\x18\x01 \x01(\x08\x1a\x1b\n\nInputFiles\x12\r\n\x05\x66iles\x18\x01 \x03(\t\x1a\x1f\n\x0cSparkVersion\x12\x0f\n\x07version\x18\x01 \x01(\t\x1a\x33\n\x08\x44\x44LParse\x12\'\n\x06parsed\x18\x01 \x01(\x0b\x32\x17.spark.connect.DataType\x1a\x1f\n\rSameSemantics\x12\x0e\n\x06result\x18\x01 \x01(\x08\x1a\x1e\n\x0cSemanticHash\x12\x0e\n\x06result\x18\x01 \x01(\x05\x1a\t\n\x07Persist\x1a\x0b\n\tUnpersist\x1a\x45\n\x0fGetStorageLevel\x12\x32\n\rstorage_level\x18\x01 \x01(\x0b\x32\x1b.spark.connect.StorageLevelB\x08\n\x06result\"\xb7\x03\n\x12\x45xecutePlanRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x30\n\x0cuser_context\x18\x02 \x01(\x0b\x32\x1a.spark.connect.UserContext\x12\x19\n\x0coperation_id\x18\x06 \x01(\tH\x00\x88\x01\x01\x12!\n\x04plan\x18\x03 \x01(\x0b\x32\x13.spark.connect.Plan\x12\x18\n\x0b\x63lient_type\x18\x04 \x01(\tH\x01\x88\x01\x01\x12H\n\x0frequest_options\x18\x05 \x03(\x0b\x32/.spark.connect.ExecutePlanRequest.RequestOption\x12\x0c\n\x04tags\x18\x07 \x03(\t\x1a\x89\x01\n\rRequestOption\x12:\n\x10reattach_options\x18\x01 \x01(\x0b\x32\x1e.spark.connect.ReattachOptionsH\x00\x12*\n\textension\x18\xe7\x07 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x10\n\x0erequest_optionB\x0f\n\r_operation_idB\x0e\n\x0c_client_type\"\x9e\x0c\n\x13\x45xecutePlanResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x14\n\x0coperation_id\x18\x0c \x01(\t\x12\x13\n\x0bresponse_id\x18\r \x01(\t\x12\x44\n\x0b\x61rrow_batch\x18\x02 \x01(\x0b\x32-.spark.connect.ExecutePlanResponse.ArrowBatchH\x00\x12Q\n\x12sql_command_result\x18\x05 \x01(\x0b\x32\x33.spark.connect.ExecutePlanResponse.SqlCommandResultH\x00\x12]\n#write_stream_operation_start_result\x18\x08 \x01(\x0b\x32..spark.connect.WriteStreamOperationStartResultH\x00\x12T\n\x1estreaming_query_command_result\x18\t \x01(\x0b\x32*.spark.connect.StreamingQueryCommandResultH\x00\x12P\n\x1cget_resources_command_result\x18\n \x01(\x0b\x32(.spark.connect.GetResourcesCommandResultH\x00\x12\x63\n&streaming_query_manager_command_result\x18\x0b \x01(\x0b\x32\x31.spark.connect.StreamingQueryManagerCommandResultH\x00\x12L\n\x0fresult_complete\x18\x0e \x01(\x0b\x32\x31.spark.connect.ExecutePlanResponse.ResultCompleteH\x00\x12*\n\textension\x18\xe7\x07 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12;\n\x07metrics\x18\x04 \x01(\x0b\x32*.spark.connect.ExecutePlanResponse.Metrics\x12L\n\x10observed_metrics\x18\x06 \x03(\x0b\x32\x32.spark.connect.ExecutePlanResponse.ObservedMetrics\x12\'\n\x06schema\x18\x07 \x01(\x0b\x32\x17.spark.connect.DataType\x1a=\n\x10SqlCommandResult\x12)\n\x08relation\x18\x01 \x01(\x0b\x32\x17.spark.connect.Relation\x1a-\n\nArrowBatch\x12\x11\n\trow_count\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x1a\xaf\x03\n\x07Metrics\x12H\n\x07metrics\x18\x01 \x03(\x0b\x32\x37.spark.connect.ExecutePlanResponse.Metrics.MetricObject\x1a\x98\x02\n\x0cMetricObject\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07plan_id\x18\x02 \x01(\x03\x12\x0e\n\x06parent\x18\x03 \x01(\x03\x12h\n\x11\x65xecution_metrics\x18\x04 \x03(\x0b\x32M.spark.connect.ExecutePlanResponse.Metrics.MetricObject.ExecutionMetricsEntry\x1ao\n\x15\x45xecutionMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.spark.connect.ExecutePlanResponse.Metrics.MetricValue:\x02\x38\x01\x1a?\n\x0bMetricValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03\x12\x13\n\x0bmetric_type\x18\x03 \x01(\t\x1aR\n\x0fObservedMetrics\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x06values\x18\x02 \x03(\x0b\x32!.spark.connect.Expression.Literal\x1a\x10\n\x0eResultCompleteB\x0f\n\rresponse_type\"5\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\x05value\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_value\"\xe5\x06\n\rConfigRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x30\n\x0cuser_context\x18\x02 \x01(\x0b\x32\x1a.spark.connect.UserContext\x12\x39\n\toperation\x18\x03 \x01(\x0b\x32&.spark.connect.ConfigRequest.Operation\x12\x18\n\x0b\x63lient_type\x18\x04 \x01(\tH\x00\x88\x01\x01\x1a\xb0\x03\n\tOperation\x12/\n\x03set\x18\x01 \x01(\x0b\x32 .spark.connect.ConfigRequest.SetH\x00\x12/\n\x03get\x18\x02 \x01(\x0b\x32 .spark.connect.ConfigRequest.GetH\x00\x12G\n\x10get_with_default\x18\x03 \x01(\x0b\x32+.spark.connect.ConfigRequest.GetWithDefaultH\x00\x12<\n\nget_option\x18\x04 \x01(\x0b\x32&.spark.connect.ConfigRequest.GetOptionH\x00\x12\x36\n\x07get_all\x18\x05 \x01(\x0b\x32#.spark.connect.ConfigRequest.GetAllH\x00\x12\x33\n\x05unset\x18\x06 \x01(\x0b\x32\".spark.connect.ConfigRequest.UnsetH\x00\x12\x42\n\ris_modifiable\x18\x07 \x01(\x0b\x32).spark.connect.ConfigRequest.IsModifiableH\x00\x42\t\n\x07op_type\x1a-\n\x03Set\x12&\n\x05pairs\x18\x01 \x03(\x0b\x32\x17.spark.connect.KeyValue\x1a\x13\n\x03Get\x12\x0c\n\x04keys\x18\x01 \x03(\t\x1a\x38\n\x0eGetWithDefault\x12&\n\x05pairs\x18\x01 \x03(\x0b\x32\x17.spark.connect.KeyValue\x1a\x19\n\tGetOption\x12\x0c\n\x04keys\x18\x01 \x03(\t\x1a(\n\x06GetAll\x12\x13\n\x06prefix\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_prefix\x1a\x15\n\x05Unset\x12\x0c\n\x04keys\x18\x01 \x03(\t\x1a\x1c\n\x0cIsModifiable\x12\x0c\n\x04keys\x18\x01 \x03(\tB\x0e\n\x0c_client_type\"^\n\x0e\x43onfigResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12&\n\x05pairs\x18\x02 \x03(\x0b\x32\x17.spark.connect.KeyValue\x12\x10\n\x08warnings\x18\x03 \x03(\t\"\xdc\x05\n\x13\x41\x64\x64\x41rtifactsRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x30\n\x0cuser_context\x18\x02 \x01(\x0b\x32\x1a.spark.connect.UserContext\x12\x18\n\x0b\x63lient_type\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\x39\n\x05\x62\x61tch\x18\x03 \x01(\x0b\x32(.spark.connect.AddArtifactsRequest.BatchH\x00\x12N\n\x0b\x62\x65gin_chunk\x18\x04 \x01(\x0b\x32\x37.spark.connect.AddArtifactsRequest.BeginChunkedArtifactH\x00\x12\x41\n\x05\x63hunk\x18\x05 \x01(\x0b\x32\x30.spark.connect.AddArtifactsRequest.ArtifactChunkH\x00\x1a*\n\rArtifactChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0b\n\x03\x63rc\x18\x02 \x01(\x03\x1a\x63\n\x13SingleChunkArtifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x30.spark.connect.AddArtifactsRequest.ArtifactChunk\x1aR\n\x05\x42\x61tch\x12I\n\tartifacts\x18\x01 \x03(\x0b\x32\x36.spark.connect.AddArtifactsRequest.SingleChunkArtifact\x1a\x96\x01\n\x14\x42\x65ginChunkedArtifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0btotal_bytes\x18\x02 \x01(\x03\x12\x12\n\nnum_chunks\x18\x03 \x01(\x03\x12G\n\rinitial_chunk\x18\x04 \x01(\x0b\x32\x30.spark.connect.AddArtifactsRequest.ArtifactChunkB\t\n\x07payloadB\x0e\n\x0c_client_type\"\x9a\x01\n\x14\x41\x64\x64\x41rtifactsResponse\x12\x46\n\tartifacts\x18\x01 \x03(\x0b\x32\x33.spark.connect.AddArtifactsResponse.ArtifactSummary\x1a:\n\x0f\x41rtifactSummary\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x11is_crc_successful\x18\x02 \x01(\x08\"\x98\x01\n\x17\x41rtifactStatusesRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x30\n\x0cuser_context\x18\x02 \x01(\x0b\x32\x1a.spark.connect.UserContext\x12\x18\n\x0b\x63lient_type\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05names\x18\x04 \x03(\tB\x0e\n\x0c_client_type\"\xee\x01\n\x18\x41rtifactStatusesResponse\x12G\n\x08statuses\x18\x01 \x03(\x0b\x32\x35.spark.connect.ArtifactStatusesResponse.StatusesEntry\x1a \n\x0e\x41rtifactStatus\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\x1ag\n\rStatusesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.spark.connect.ArtifactStatusesResponse.ArtifactStatus:\x02\x38\x01\"\x8a\x03\n\x10InterruptRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x30\n\x0cuser_context\x18\x02 \x01(\x0b\x32\x1a.spark.connect.UserContext\x12\x18\n\x0b\x63lient_type\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x45\n\x0einterrupt_type\x18\x04 \x01(\x0e\x32-.spark.connect.InterruptRequest.InterruptType\x12\x17\n\roperation_tag\x18\x05 \x01(\tH\x00\x12\x16\n\x0coperation_id\x18\x06 \x01(\tH\x00\"\x80\x01\n\rInterruptType\x12\x1e\n\x1aINTERRUPT_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12INTERRUPT_TYPE_ALL\x10\x01\x12\x16\n\x12INTERRUPT_TYPE_TAG\x10\x02\x12\x1f\n\x1bINTERRUPT_TYPE_OPERATION_ID\x10\x03\x42\x0b\n\tinterruptB\x0e\n\x0c_client_type\"@\n\x11InterruptResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x17\n\x0finterrupted_ids\x18\x02 \x03(\t\"\'\n\x0fReattachOptions\x12\x14\n\x0creattachable\x18\x01 \x01(\x08\"\xd2\x01\n\x16ReattachExecuteRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x30\n\x0cuser_context\x18\x02 \x01(\x0b\x32\x1a.spark.connect.UserContext\x12\x14\n\x0coperation_id\x18\x03 \x01(\t\x12\x18\n\x0b\x63lient_type\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10last_response_id\x18\x05 \x01(\tH\x01\x88\x01\x01\x42\x0e\n\x0c_client_typeB\x13\n\x11_last_response_id\"\xef\x02\n\x15ReleaseExecuteRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x30\n\x0cuser_context\x18\x02 \x01(\x0b\x32\x1a.spark.connect.UserContext\x12\x14\n\x0coperation_id\x18\x03 \x01(\t\x12\x18\n\x0b\x63lient_type\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x46\n\x0brelease_all\x18\x05 \x01(\x0b\x32/.spark.connect.ReleaseExecuteRequest.ReleaseAllH\x00\x12J\n\rrelease_until\x18\x06 \x01(\x0b\x32\x31.spark.connect.ReleaseExecuteRequest.ReleaseUntilH\x00\x1a\x0c\n\nReleaseAll\x1a#\n\x0cReleaseUntil\x12\x13\n\x0bresponse_id\x18\x01 \x01(\tB\t\n\x07releaseB\x0e\n\x0c_client_type\"X\n\x16ReleaseExecuteResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x19\n\x0coperation_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0f\n\r_operation_id2\xe7\x05\n\x13SparkConnectService\x12X\n\x0b\x45xecutePlan\x12!.spark.connect.ExecutePlanRequest\x1a\".spark.connect.ExecutePlanResponse\"\x00\x30\x01\x12V\n\x0b\x41nalyzePlan\x12!.spark.connect.AnalyzePlanRequest\x1a\".spark.connect.AnalyzePlanResponse\"\x00\x12G\n\x06\x43onfig\x12\x1c.spark.connect.ConfigRequest\x1a\x1d.spark.connect.ConfigResponse\"\x00\x12[\n\x0c\x41\x64\x64\x41rtifacts\x12\".spark.connect.AddArtifactsRequest\x1a#.spark.connect.AddArtifactsResponse\"\x00(\x01\x12\x63\n\x0e\x41rtifactStatus\x12&.spark.connect.ArtifactStatusesRequest\x1a\'.spark.connect.ArtifactStatusesResponse\"\x00\x12P\n\tInterrupt\x12\x1f.spark.connect.InterruptRequest\x1a .spark.connect.InterruptResponse\"\x00\x12`\n\x0fReattachExecute\x12%.spark.connect.ReattachExecuteRequest\x1a\".spark.connect.ExecutePlanResponse\"\x00\x30\x01\x12_\n\x0eReleaseExecute\x12$.spark.connect.ReleaseExecuteRequest\x1a%.spark.connect.ReleaseExecuteResponse\"\x00\x42\x36\n\x1eorg.apache.spark.connect.protoP\x01Z\x12internal/generatedb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spark.connect.base_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036org.apache.spark.connect.protoP\001Z\022internal/generated'
  _globals['_EXECUTEPLANRESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY']._options = None
  _globals['_EXECUTEPLANRESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY']._serialized_options = b'8\001'
  _globals['_ARTIFACTSTATUSESRESPONSE_STATUSESENTRY']._options = None
  _globals['_ARTIFACTSTATUSESRESPONSE_STATUSESENTRY']._serialized_options = b'8\001'
  _globals['_PLAN']._serialized_start=219
  _globals['_PLAN']._serialized_end=320
  _globals['_USERCONTEXT']._serialized_start=322
  _globals['_USERCONTEXT']._serialized_end=414
  _globals['_ANALYZEPLANREQUEST']._serialized_start=417
  _globals['_ANALYZEPLANREQUEST']._serialized_end=2498
  _globals['_ANALYZEPLANREQUEST_SCHEMA']._serialized_start=1423
  _globals['_ANALYZEPLANREQUEST_SCHEMA']._serialized_end=1466
  _globals['_ANALYZEPLANREQUEST_EXPLAIN']._serialized_start=1469
  _globals['_ANALYZEPLANREQUEST_EXPLAIN']._serialized_end=1765
  _globals['_ANALYZEPLANREQUEST_EXPLAIN_EXPLAINMODE']._serialized_start=1593
  _globals['_ANALYZEPLANREQUEST_EXPLAIN_EXPLAINMODE']._serialized_end=1765
  _globals['_ANALYZEPLANREQUEST_TREESTRING']._serialized_start=1767
  _globals['_ANALYZEPLANREQUEST_TREESTRING']._serialized_end=1844
  _globals['_ANALYZEPLANREQUEST_ISLOCAL']._serialized_start=1846
  _globals['_ANALYZEPLANREQUEST_ISLOCAL']._serialized_end=1890
  _globals['_ANALYZEPLANREQUEST_ISSTREAMING']._serialized_start=1892
  _globals['_ANALYZEPLANREQUEST_ISSTREAMING']._serialized_end=1940
  _globals['_ANALYZEPLANREQUEST_INPUTFILES']._serialized_start=1942
  _globals['_ANALYZEPLANREQUEST_INPUTFILES']._serialized_end=1989
  _globals['_ANALYZEPLANREQUEST_SPARKVERSION']._serialized_start=1991
  _globals['_ANALYZEPLANREQUEST_SPARKVERSION']._serialized_end=2005
  _globals['_ANALYZEPLANREQUEST_DDLPARSE']._serialized_start=2007
  _globals['_ANALYZEPLANREQUEST_DDLPARSE']._serialized_end=2037
  _globals['_ANALYZEPLANREQUEST_SAMESEMANTICS']._serialized_start=2039
  _globals['_ANALYZEPLANREQUEST_SAMESEMANTICS']._serialized_end=2137
  _globals['_ANALYZEPLANREQUEST_SEMANTICHASH']._serialized_start=2139
  _globals['_ANALYZEPLANREQUEST_SEMANTICHASH']._serialized_end=2188
  _globals['_ANALYZEPLANREQUEST_PERSIST']._serialized_start=2190
  _globals['_ANALYZEPLANREQUEST_PERSIST']._serialized_end=2317
  _globals['_ANALYZEPLANREQUEST_UNPERSIST']._serialized_start=2319
  _globals['_ANALYZEPLANREQUEST_UNPERSIST']._serialized_end=2409
  _globals['_ANALYZEPLANREQUEST_GETSTORAGELEVEL']._serialized_start=2411
  _globals['_ANALYZEPLANREQUEST_GETSTORAGELEVEL']._serialized_end=2471
  _globals['_ANALYZEPLANRESPONSE']._serialized_start=2501
  _globals['_ANALYZEPLANRESPONSE']._serialized_end=3915
  _globals['_ANALYZEPLANRESPONSE_SCHEMA']._serialized_start=3445
  _globals['_ANALYZEPLANRESPONSE_SCHEMA']._serialized_end=3494
  _globals['_ANALYZEPLANRESPONSE_EXPLAIN']._serialized_start=3496
  _globals['_ANALYZEPLANRESPONSE_EXPLAIN']._serialized_end=3529
  _globals['_ANALYZEPLANRESPONSE_TREESTRING']._serialized_start=3531
  _globals['_ANALYZEPLANRESPONSE_TREESTRING']._serialized_end=3564
  _globals['_ANALYZEPLANRESPONSE_ISLOCAL']._serialized_start=3566
  _globals['_ANALYZEPLANRESPONSE_ISLOCAL']._serialized_end=3593
  _globals['_ANALYZEPLANRESPONSE_ISSTREAMING']._serialized_start=3595
  _globals['_ANALYZEPLANRESPONSE_ISSTREAMING']._serialized_end=3630
  _globals['_ANALYZEPLANRESPONSE_INPUTFILES']._serialized_start=3632
  _globals['_ANALYZEPLANRESPONSE_INPUTFILES']._serialized_end=3659
  _globals['_ANALYZEPLANRESPONSE_SPARKVERSION']._serialized_start=3661
  _globals['_ANALYZEPLANRESPONSE_SPARKVERSION']._serialized_end=3692
  _globals['_ANALYZEPLANRESPONSE_DDLPARSE']._serialized_start=3694
  _globals['_ANALYZEPLANRESPONSE_DDLPARSE']._serialized_end=3745
  _globals['_ANALYZEPLANRESPONSE_SAMESEMANTICS']._serialized_start=3747
  _globals['_ANALYZEPLANRESPONSE_SAMESEMANTICS']._serialized_end=3778
  _globals['_ANALYZEPLANRESPONSE_SEMANTICHASH']._serialized_start=3780
  _globals['_ANALYZEPLANRESPONSE_SEMANTICHASH']._serialized_end=3810
  _globals['_ANALYZEPLANRESPONSE_PERSIST']._serialized_start=2190
  _globals['_ANALYZEPLANRESPONSE_PERSIST']._serialized_end=2199
  _globals['_ANALYZEPLANRESPONSE_UNPERSIST']._serialized_start=2319
  _globals['_ANALYZEPLANRESPONSE_UNPERSIST']._serialized_end=2330
  _globals['_ANALYZEPLANRESPONSE_GETSTORAGELEVEL']._serialized_start=3836
  _globals['_ANALYZEPLANRESPONSE_GETSTORAGELEVEL']._serialized_end=3905
  _globals['_EXECUTEPLANREQUEST']._serialized_start=3918
  _globals['_EXECUTEPLANREQUEST']._serialized_end=4357
  _globals['_EXECUTEPLANREQUEST_REQUESTOPTION']._serialized_start=4187
  _globals['_EXECUTEPLANREQUEST_REQUESTOPTION']._serialized_end=4324
  _globals['_EXECUTEPLANRESPONSE']._serialized_start=4360
  _globals['_EXECUTEPLANRESPONSE']._serialized_end=5926
  _globals['_EXECUTEPLANRESPONSE_SQLCOMMANDRESULT']._serialized_start=5265
  _globals['_EXECUTEPLANRESPONSE_SQLCOMMANDRESULT']._serialized_end=5326
  _globals['_EXECUTEPLANRESPONSE_ARROWBATCH']._serialized_start=5328
  _globals['_EXECUTEPLANRESPONSE_ARROWBATCH']._serialized_end=5373
  _globals['_EXECUTEPLANRESPONSE_METRICS']._serialized_start=5376
  _globals['_EXECUTEPLANRESPONSE_METRICS']._serialized_end=5807
  _globals['_EXECUTEPLANRESPONSE_METRICS_METRICOBJECT']._serialized_start=5462
  _globals['_EXECUTEPLANRESPONSE_METRICS_METRICOBJECT']._serialized_end=5742
  _globals['_EXECUTEPLANRESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY']._serialized_start=5631
  _globals['_EXECUTEPLANRESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY']._serialized_end=5742
  _globals['_EXECUTEPLANRESPONSE_METRICS_METRICVALUE']._serialized_start=5744
  _globals['_EXECUTEPLANRESPONSE_METRICS_METRICVALUE']._serialized_end=5807
  _globals['_EXECUTEPLANRESPONSE_OBSERVEDMETRICS']._serialized_start=5809
  _globals['_EXECUTEPLANRESPONSE_OBSERVEDMETRICS']._serialized_end=5891
  _globals['_EXECUTEPLANRESPONSE_RESULTCOMPLETE']._serialized_start=5893
  _globals['_EXECUTEPLANRESPONSE_RESULTCOMPLETE']._serialized_end=5909
  _globals['_KEYVALUE']._serialized_start=5928
  _globals['_KEYVALUE']._serialized_end=5981
  _globals['_CONFIGREQUEST']._serialized_start=5984
  _globals['_CONFIGREQUEST']._serialized_end=6853
  _globals['_CONFIGREQUEST_OPERATION']._serialized_start=6157
  _globals['_CONFIGREQUEST_OPERATION']._serialized_end=6589
  _globals['_CONFIGREQUEST_SET']._serialized_start=6591
  _globals['_CONFIGREQUEST_SET']._serialized_end=6636
  _globals['_CONFIGREQUEST_GET']._serialized_start=6638
  _globals['_CONFIGREQUEST_GET']._serialized_end=6657
  _globals['_CONFIGREQUEST_GETWITHDEFAULT']._serialized_start=6659
  _globals['_CONFIGREQUEST_GETWITHDEFAULT']._serialized_end=6715
  _globals['_CONFIGREQUEST_GETOPTION']._serialized_start=6717
  _globals['_CONFIGREQUEST_GETOPTION']._serialized_end=6742
  _globals['_CONFIGREQUEST_GETALL']._serialized_start=6744
  _globals['_CONFIGREQUEST_GETALL']._serialized_end=6784
  _globals['_CONFIGREQUEST_UNSET']._serialized_start=6786
  _globals['_CONFIGREQUEST_UNSET']._serialized_end=6807
  _globals['_CONFIGREQUEST_ISMODIFIABLE']._serialized_start=6809
  _globals['_CONFIGREQUEST_ISMODIFIABLE']._serialized_end=6837
  _globals['_CONFIGRESPONSE']._serialized_start=6855
  _globals['_CONFIGRESPONSE']._serialized_end=6949
  _globals['_ADDARTIFACTSREQUEST']._serialized_start=6952
  _globals['_ADDARTIFACTSREQUEST']._serialized_end=7684
  _globals['_ADDARTIFACTSREQUEST_ARTIFACTCHUNK']._serialized_start=7277
  _globals['_ADDARTIFACTSREQUEST_ARTIFACTCHUNK']._serialized_end=7319
  _globals['_ADDARTIFACTSREQUEST_SINGLECHUNKARTIFACT']._serialized_start=7321
  _globals['_ADDARTIFACTSREQUEST_SINGLECHUNKARTIFACT']._serialized_end=7420
  _globals['_ADDARTIFACTSREQUEST_BATCH']._serialized_start=7422
  _globals['_ADDARTIFACTSREQUEST_BATCH']._serialized_end=7504
  _globals['_ADDARTIFACTSREQUEST_BEGINCHUNKEDARTIFACT']._serialized_start=7507
  _globals['_ADDARTIFACTSREQUEST_BEGINCHUNKEDARTIFACT']._serialized_end=7657
  _globals['_ADDARTIFACTSRESPONSE']._serialized_start=7687
  _globals['_ADDARTIFACTSRESPONSE']._serialized_end=7841
  _globals['_ADDARTIFACTSRESPONSE_ARTIFACTSUMMARY']._serialized_start=7783
  _globals['_ADDARTIFACTSRESPONSE_ARTIFACTSUMMARY']._serialized_end=7841
  _globals['_ARTIFACTSTATUSESREQUEST']._serialized_start=7844
  _globals['_ARTIFACTSTATUSESREQUEST']._serialized_end=7996
  _globals['_ARTIFACTSTATUSESRESPONSE']._serialized_start=7999
  _globals['_ARTIFACTSTATUSESRESPONSE']._serialized_end=8237
  _globals['_ARTIFACTSTATUSESRESPONSE_ARTIFACTSTATUS']._serialized_start=8100
  _globals['_ARTIFACTSTATUSESRESPONSE_ARTIFACTSTATUS']._serialized_end=8132
  _globals['_ARTIFACTSTATUSESRESPONSE_STATUSESENTRY']._serialized_start=8134
  _globals['_ARTIFACTSTATUSESRESPONSE_STATUSESENTRY']._serialized_end=8237
  _globals['_INTERRUPTREQUEST']._serialized_start=8240
  _globals['_INTERRUPTREQUEST']._serialized_end=8634
  _globals['_INTERRUPTREQUEST_INTERRUPTTYPE']._serialized_start=8477
  _globals['_INTERRUPTREQUEST_INTERRUPTTYPE']._serialized_end=8605
  _globals['_INTERRUPTRESPONSE']._serialized_start=8636
  _globals['_INTERRUPTRESPONSE']._serialized_end=8700
  _globals['_REATTACHOPTIONS']._serialized_start=8702
  _globals['_REATTACHOPTIONS']._serialized_end=8741
  _globals['_REATTACHEXECUTEREQUEST']._serialized_start=8744
  _globals['_REATTACHEXECUTEREQUEST']._serialized_end=8954
  _globals['_RELEASEEXECUTEREQUEST']._serialized_start=8957
  _globals['_RELEASEEXECUTEREQUEST']._serialized_end=9324
  _globals['_RELEASEEXECUTEREQUEST_RELEASEALL']._serialized_start=9248
  _globals['_RELEASEEXECUTEREQUEST_RELEASEALL']._serialized_end=9260
  _globals['_RELEASEEXECUTEREQUEST_RELEASEUNTIL']._serialized_start=9262
  _globals['_RELEASEEXECUTEREQUEST_RELEASEUNTIL']._serialized_end=9297
  _globals['_RELEASEEXECUTERESPONSE']._serialized_start=9326
  _globals['_RELEASEEXECUTERESPONSE']._serialized_end=9414
  _globals['_SPARKCONNECTSERVICE']._serialized_start=9417
  _globals['_SPARKCONNECTSERVICE']._serialized_end=10160
# @@protoc_insertion_point(module_scope)