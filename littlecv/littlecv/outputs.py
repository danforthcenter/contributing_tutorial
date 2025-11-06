class Outputs:
    """littlecv outputs, simplified from PlantCV outputs class"""

    def __init__(self):
        self.measurements = {}
        self.images = []
        self.observations = {}
        self.metadata = {}

     # Method to add observation to outputs
    def add_observation(self, sample, variable, trait, method, scale, datatype, value, label):
        """Keyword arguments/parameters:
        sample       = Sample name. Used to distinguish between multiple samples
        variable     = A local unique identifier of a variable, e.g. a short name,
                       that is a key linking the definitions of variables with observations.
        trait        = A name of the trait mapped to an external ontology; if there is no exact mapping, an informative
                       description of the trait.
        method       = A name of the measurement method mapped to an external ontology; if there is no exact mapping, an
                       informative description of the measurement procedure
        scale        = Units of the measurement or scale in which the observations are expressed; if possible, standard
                       units and scales should be used and mapped to existing ontologies; in the case of non-standard
                       scale a full explanation should be given
        datatype     = The type of data to be stored, e.g. 'int', 'float', 'str', 'list', 'bool', etc.
        value        = The data itself
        label        = The label for each value (most useful when the data is a frequency table as in hue,
                       or other tables)

        :param sample: str
        :param variable: str
        :param trait: str
        :param method: str
        :param scale: str
        :param datatype: type
        :param value:
        :param label:
        """
        # Create an empty dictionary for the sample if it does not exist
        if sample not in self.observations:
            self.observations[sample] = {}

        # Save the observation for the sample and variable
        self.observations[sample][variable] = {
            "trait": trait,
            "method": method,
            "scale": scale,
            "datatype": str(datatype),
            "value": value,
            "label": label
        }

    def add_metadata(self, term, datatype, value):
        """Add a metadata term and value to outputs.
        Parameters
        ----------
        term : str
              Metadata term/name.
        datatype : type
              The type of data to be stored, e.g. 'int', 'float', 'str', 'list', 'bool', etc.
        value : any
              The data itself.
        """
        # Create an empty dictionary for the sample if it does not exist
        if term not in self.metadata:
            self.metadata[term] = {}
        # Save the observation for the sample and variable
        self.metadata[term] = {
            "datatype": str(datatype),
            "value": [value]
        }
