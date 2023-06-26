from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import message

@dataclass
class SendMailPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Message property
    message: Optional[message.Message] = None
    # The SaveToSentItems property
    save_to_sent_items: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SendMailPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SendMailPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SendMailPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models import message

        from ...models import message

        fields: Dict[str, Callable[[Any], None]] = {
            "Message": lambda n : setattr(self, 'message', n.get_object_value(message.Message)),
            "SaveToSentItems": lambda n : setattr(self, 'save_to_sent_items', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("Message", self.message)
        writer.write_bool_value("SaveToSentItems", self.save_to_sent_items)
        writer.write_additional_data_value(self.additional_data)
    
