from pydantic import BaseModel
from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field, field_validator


class MySettings(BaseModel):
    n_of_chunks: int = 5

@plugin
def settings_schema():
    return MySettings.schema()
    
