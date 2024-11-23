class Television:
    # Class variables (constants)
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes the television with default values.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__previous_volume: int = Television.MIN_VOLUME  # Store previous volume before muting
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turns the television on/off by changing the status.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes and unmutes the television. When the TV is muted, set the volume to 0.
        If muted, adjusting volume will unmute the TV and adjust volume accordingly.
        """
        if self.__status:
            if self.__muted:
                # Unmute and restore previous volume
                self.__muted = False
                self.__volume = self.__previous_volume
            else:
                # Mute and save current volume before muting
                self.__muted = True
                self.__previous_volume = self.__volume  # Save current volume before muting
                self.__volume = Television.MIN_VOLUME  # Mute by setting volume to 0

    def channel_up(self) -> None:
        """
        Increases the channel value. If the TV is on the max channel, it resets to the min channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the channel value. If the TV is on the min channel, it resets to the max channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume. If the TV is at max volume, it stays at max.
        If the TV is muted, unmute it and increase volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume  # Unmute and restore previous volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume. If the TV is at min volume, it stays at min.
        If the TV is muted, unmute it and decrease volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume  # Unmute and restore previous volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns the current state of the television in string format.
        """
        return f"Power: {self.__status}, Channel: {self.__channel}, Volume: {self.__volume}"


