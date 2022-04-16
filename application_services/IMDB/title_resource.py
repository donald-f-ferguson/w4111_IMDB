from DFF_Framework.rdb_base_application_resource import BaseRDBApplicationResource


class TitleResource(BaseRDBApplicationResource):

    def __init__(self, config_info):
        super().__init__(config_info)

    def get_links(self, resource_data):
        """

        Generate the links section of the GET with query parameters response. Currently, each resource
        implementation MUST implement the method with logic specific to the resource implementation.

        :param resource_data: A list of resources from the collection.
        :return: The list of resources with a links [] section added. The links section provides links to
            related resources that can be located using values in the resources in the collection. For example,
            if a resource in the list has a pair {"address_id": 121}, this method might add an entry of the form
            {"rel": "address", "href": "/addresses/121"}
        """

        # DFF TODO We can move into base class by including link info in config.
        # Sometimes you have to stop the madness.

        for r in resource_data:
            nc = r['tconst']

            links = []
            self_link = {"rel": "self", "href": "/api/titles/" + str(nc)}
            links.append(self_link)

            r["links"] = links

        return resource_data

    def create(self, new_resource_info):
        """

        :param new_resource_info: The fields and values for the new resource.
        :return: The ID of the User created.
        """
        db_svc = self._get_db_resource()

        """
        This is an example of simple application logic. In many cases, I could push basic validity logic into
        the database engine if it supports constraints, not NULL, ... ... More complex logic requires code in the
        resource implementation.
        """
        email = new_resource_info.get("email", None)
        if email is None or not '@' in email:
            raise ValueError("Invalid email address.")

        # This logic is specific to this resource. The data in the DB contains a set of IDs for users.
        # The new resource has to have the next largest ID.
        next_id = db_svc.get_next_id()

        new_resource_info["id"] = next_id

        res = super().create(new_resource_info)

        return next_id

    def get_by_prefix(self, prefix):

        db_svc = self._get_db_resource()
        res = db_svc.get_from_prefix()
