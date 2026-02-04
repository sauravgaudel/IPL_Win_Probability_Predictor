# Backend/schemas/input.py
from pydantic import BaseModel, Field, computed_field
from typing import Annotated

class Input(BaseModel):
    batting_team: Annotated[str, Field(...)]
    bowling_team: Annotated[str, Field(...)]
    city: Annotated[str, Field(...)]
    total_run_x: Annotated[int, Field(..., gt=0)]
    current_score: Annotated[int, Field(..., gt=-1)]
    overs_completed: Annotated[float, Field(..., gt=0, lt=20)]
    wicket_fallen: Annotated[int, Field(..., gt=-1, lt=10)]

    @computed_field
    @property
    def runs_left(self) -> int:
        return self.total_run_x - self.current_score

    @computed_field
    @property
    def balls_left(self) -> int:
        return 120 - (int(self.overs_completed)*6 + int((self.overs_completed - int(self.overs_completed))*10))

    @computed_field
    @property
    def wickets_left(self) -> int:
        return 10 - self.wicket_fallen

    @computed_field
    @property
    def CRR(self) -> float:
        return self.current_score / self.overs_completed

    @computed_field
    @property
    def RRR(self) -> float:
        return self.runs_left / (self.balls_left / 6)
