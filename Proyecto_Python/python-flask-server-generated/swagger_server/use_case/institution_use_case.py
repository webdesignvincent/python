from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData
from swagger_server.models.request_institution_add import RequestInstitutionAdd


class InstitutionUseCase:

    def __init__(self, institution_repository):
        self.institution_repository = institution_repository

    def get_institution(self):
        data_response = []
        institutions = self.institution_repository.get_institution()

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                    status=i.status,
                )
            )

        response = ResponseInstitution(
            code=200,
            message="Proceso exitoso",
            data=data_response
        )

        return response

    def get_institution_by_id(self,id):
        data_response = []
        institutions = self.institution_repository.get_institution_by_id(id)
        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                    created_user=i.created_user,
                    status=i.status,
                )
            )
        
        response = ResponseInstitution(
            code=200,
            message="Proceso exitoso",
            data=data_response
        )

        return response
