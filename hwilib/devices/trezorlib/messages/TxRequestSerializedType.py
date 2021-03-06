# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class TxRequestSerializedType(p.MessageType):

    def __init__(
        self,
        signature_index: int = None,
        signature: bytes = None,
        serialized_tx: bytes = None,
    ) -> None:
        self.signature_index = signature_index
        self.signature = signature
        self.serialized_tx = serialized_tx

    @classmethod
    def get_fields(cls):
        return {
            1: ('signature_index', p.UVarintType, 0),
            2: ('signature', p.BytesType, 0),
            3: ('serialized_tx', p.BytesType, 0),
        }
