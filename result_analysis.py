from workload import WorkLoad

class ExecResult(object):
    """
    Analysis class
    """
    def __init__(self, workload):
        """
        Constructor
        """
        self.workload = workload
        self.workload.set_analysis(self)
        self.workload.set_analysis_name(self.__class__.__name__)
        self.workload.set_analysis_description(self.__class__.__doc__)
        self.workload.set_analysis_version("0.1")
        self.workload.set_analysis_author("Marcos Alvarez")
        self.workload.set_analysis_email("marcos.alvarez@us.es")
        self.workload.set_analysis_date("2014-04-01")
        self.workload.set_analysis_copyright("Copyright (c) 2014 Marcos Alvarez")

    def run(self):
        """
        Run analysis
        """
        pass

    def get_workload(self):
        """
        Return workload
        """
        return self.workload

    def set_workload(self, workload):
        """
        Set workload
        """
        self.workload = workload

    def get_workload_name(self):
        """
        Return workload name
        """
        return self.workload.get_workload_name()

    def set_workload_name(self, workload_name):
        """
        Set workload name
        """
        self.workload.set_workload_name(workload_name)

    def get_workload_description(self):
        """
        Return workload description
        """
        return self.workload.get_workload_description()

    def set_workload_description(self, workload_description):
        """
        Set workload description
        """
        self.workload.set_workload_description(workload_description)
    def get_workload_analysis_date(self):
        """
        Return workload analysis date
        """
        return self.workload.get_analysis_date()

    def set_workload_analysis_date(self, workload_analysis_date):
        """
        Set workload analysis date
        """
        self.workload.set_analysis_date(workload_analysis_date)

    def get_workload_analysis_email(self):
        """
        Return workload analysis email
        """
        return self.workload.get_analysis_email()

    def set_workload_analysis_email(self, workload_analysis_email):
        """
        Set workload analysis email
        """
        self.workload.set_analysis_email(workload_analysis_email)

    def get_workload_analysis_method(self):
        """
        Return workload analysis method
        """
        return self.workload.get_analysis_method()

    def set_workload_analysis_method(self, workload_analysis_method):
        """
        Set workload analysis method
        """
        self.workload.set_analysis_method(workload_analysis_method)

    def get_workload_analysis_type(self):
        """
        Return workload analysis type
        """
        return self.workload.get_analysis_type()

    def set_workload_analysis_type(self, workload_analysis_type):
        """
        Set workload analysis type
        """
        self.workload.set_analysis_type(workload_analysis_type)

    def get_workload_analysis_url(self):
        """
        Return workload analysis url
        """
        return self.workload.get_analysis_url()

    def set_workload_analysis_url(self, workload_analysis_url):
        """
        Set workload analysis url
        """
        self.workload.set_analysis_url(workload_analysis_url)

    def get_workload_analysis_user(self):
        """
        Return workload analysis user
        """
        return self.workload.get_analysis_user()

    def set_workload_analysis_user(self, workload_analysis_user):
        """
        Set workload analysis user
        """
        self.workload.set_analysis_user(workload_analysis_user)

    def get_workload_analysis_password(self):
        """
        Return workload analysis password
        """
        return self.workload.get_analysis_password()

    def set_workload_analysis_password(self, workload_analysis_password):
        """
        Set workload analysis password
        """
        self.workload.set_analysis_password(workload_analysis_password)
