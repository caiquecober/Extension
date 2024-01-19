### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from openbb_core.app.static.container import Container
from openbb_core.app.model.obbject import OBBject
from typing import Dict, Optional
from openbb_core.app.static.utils.decorators import validate

from openbb_core.app.static.utils.filters import filter_inputs


class ROUTER_eia(Container):
    """/eia
    dataseries
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate
    def dataseries(
        self,
        series: str = "PET.WCRRIUS2.W",
        credentials: Optional[Dict[str, str]] = None,
    ) -> OBBject:
        """Get EIA Data"""  # noqa: E501

        return self._run(
            "/eia/dataseries",
            **filter_inputs(
                series=series,
                credentials=credentials,
            )
        )
