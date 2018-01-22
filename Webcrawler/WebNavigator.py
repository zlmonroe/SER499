class WebNavigator(object):
    """Defines methods for navigating web links"""

    @staticmethod
    def getContent(link):
        """
        Retrieves the content from a link

        :param link: An absolute URL
        """
        return ""

    @staticmethod
    def getLinks(link):
        """
        Finds all links contained on a page from a link

        :param str link: An absolute URL
        """
        return []

    @staticmethod
    def limitDomain(links, domain):
        """
        Prunes all links outside of a given domain

        :param links A list of links
        :type links: list of strings
        :param str domain: The domain used to filter the links
        :return: A filtered list of links
        :rtype list of strings
        """
        return []

    @staticmethod
    def getAbsolute(ResolvedParent, RelativeLink):
        """
        Creates an absolute URL from a link and its parent

        :param str ResolvedParent: Any resolved parent URL
        :param str RelativeLink: A relative URL
        :return: The absolute URL of the relative URL
        :rtype: str
        """
        return ""
