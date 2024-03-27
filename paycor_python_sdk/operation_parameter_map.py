operation_parameter_map = {
    '/v1/legalentities/{legalEntityId}/taxes-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalEntities/{legalEntityId}/ats/{atsAccountId}/jobs-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'atsAccountId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'postedToCareers'
            },
            {
                'name': 'status'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalEntities/{legalEntityId}/ats/{atsAccountId}/jobs/{atsJobId}-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'atsAccountId'
            },
            {
                'name': 'atsJobId'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/v1/legalEntities/{legalEntityId}/ats/accounts-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/schedules-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'StartDateTime'
            },
            {
                'name': 'EndDateTime'
            },
            {
                'name': 'BeforeStartTimeInMinutes'
            },
            {
                'name': 'AfterEndTimeInMinutes'
            },
            {
                'name': 'Label'
            },
            {
                'name': 'ShiftDepeartmentId'
            },
        ]
    },
    '/v1/employees/{employeeId}/schedules/{scheduleId}-DELETE': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'scheduleId'
            },
        ]
    },
    '/v1/employees/{employeeId}/schedules-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
        ]
    },
    '/v1/legalEntities/{legalEntityId}/schedules-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/certifications-POST': {
        'parameters': [
            {
                'name': 'CertificationName'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'EffectiveDate'
            },
            {
                'name': 'ExpirationDate'
            },
            {
                'name': 'CertificationNumber'
            },
            {
                'name': 'CertificationOrganizationName'
            },
            {
                'name': 'Notes'
            },
        ]
    },
    '/v1/employees/{employeeId}/certifications-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/certifications-PUT': {
        'parameters': [
            {
                'name': 'EmployeeCertificationId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'CertificationNumber'
            },
            {
                'name': 'EffectiveDate'
            },
            {
                'name': 'ExpirationDate'
            },
            {
                'name': 'Notes'
            },
        ]
    },
    '/v1/employees/{employeeId}/customfields-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/customfields-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
        ]
    },
    '/v1/employees/{employeeId}/deductions-POST': {
        'parameters': [
            {
                'name': 'Code'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'OnHold'
            },
            {
                'name': 'Frequency'
            },
            {
                'name': 'IncludeInPay'
            },
            {
                'name': 'AmountData'
            },
        ]
    },
    '/v1/employees/{employeeId}/deductions-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/deductions/{employeeDeductionId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'employeeDeductionId'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/v1/employees/{employeeId}/deductions-PUT': {
        'parameters': [
            {
                'name': 'Id'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'IncludeInPay'
            },
            {
                'name': 'Frequency'
            },
            {
                'name': 'OnHold'
            },
            {
                'name': 'AmountData'
            },
        ]
    },
    '/v1/employees/{employeeId}/DirectDeposits-POST': {
        'parameters': [
            {
                'name': 'AccountType'
            },
            {
                'name': 'Frequency'
            },
            {
                'name': 'OnHold'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'AccountNumber'
            },
            {
                'name': 'RoutingNumber'
            },
            {
                'name': 'DeductionCode'
            },
            {
                'name': 'DirectDepositType'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'Rate'
            },
        ]
    },
    '/v1/employees/{employeeId}/HSAaccounts-POST': {
        'parameters': [
            {
                'name': 'AccountType'
            },
            {
                'name': 'Frequency'
            },
            {
                'name': 'DeductionCode'
            },
            {
                'name': 'OnHold'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'AccountNumber'
            },
            {
                'name': 'RoutingNumber'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'Rate'
            },
        ]
    },
    '/v1/employees/{employeeId}/DirectDeposits/{directDepositId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'directDepositId'
            },
        ]
    },
    '/v1/employees/{employeeId}/DirectDeposits-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/HSAaccounts-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/DirectDeposits-PUT': {
        'parameters': [
            {
                'name': 'Id'
            },
            {
                'name': 'AccountType'
            },
            {
                'name': 'AccountNumber'
            },
            {
                'name': 'RoutingNumber'
            },
            {
                'name': 'Frequency'
            },
            {
                'name': 'OnHold'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'DirectDepositType'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'Rate'
            },
        ]
    },
    '/v1/employees/{employeeId}/HSAaccounts-PUT': {
        'parameters': [
            {
                'name': 'Id'
            },
            {
                'name': 'AccountType'
            },
            {
                'name': 'AccountNumber'
            },
            {
                'name': 'RoutingNumber'
            },
            {
                'name': 'Frequency'
            },
            {
                'name': 'OnHold'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'Rate'
            },
        ]
    },
    '/v1/employees/{employeeId}/PayStubDocument/{documentId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'documentId'
            },
        ]
    },
    '/v1/employees/{employeeId}/paystubDocumentData-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/earnings-POST': {
        'parameters': [
            {
                'name': 'Code'
            },
            {
                'name': 'AmountData'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'Frequency'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'IncludeInPay'
            },
            {
                'name': 'OnHold'
            },
        ]
    },
    '/v1/employees/{employeeId}/earnings/{employeeEarningId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'employeeEarningId'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/v1/employees/{employeeId}/earnings-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/earnings-PUT': {
        'parameters': [
            {
                'name': 'Id'
            },
            {
                'name': 'Code'
            },
            {
                'name': 'Frequency'
            },
            {
                'name': 'IncludeInPay'
            },
            {
                'name': 'OnHold'
            },
            {
                'name': 'AmountData'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'SequenceNumber'
            },
        ]
    },
    '/v1/employees/{employeeId}/emergencycontact-POST': {
        'parameters': [
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'MiddleName'
            },
            {
                'name': 'Relationship'
            },
            {
                'name': 'HomePhone'
            },
            {
                'name': 'WorkPhone'
            },
            {
                'name': 'WorkPhoneExtension'
            },
            {
                'name': 'MobilePhone'
            },
            {
                'name': 'EmailAddress'
            },
        ]
    },
    '/v1/employees/{employeeId}/I9Verification-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/v1/employees/{employeeId}/I9Verification-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'CitizenOfCountry'
            },
            {
                'name': 'WorkEligibility'
            },
            {
                'name': 'WorkVisaType'
            },
            {
                'name': 'WorkVisaExpirationDate'
            },
            {
                'name': 'AlienAdmissionNumber'
            },
            {
                'name': 'AlienAdmissionExpirationDate'
            },
            {
                'name': 'ListA'
            },
            {
                'name': 'ListB'
            },
            {
                'name': 'ListC'
            },
            {
                'name': 'ForeignPassportNumber'
            },
            {
                'name': 'CountryOfIssuance'
            },
            {
                'name': 'AdditionalInformation'
            },
        ]
    },
    '/v1/employees/onboarding-POST': {
        'parameters': [
            {
                'name': 'LegalEntityId'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'HomeEmailAddress'
            },
            {
                'name': 'ExportedByEmailAddress'
            },
            {
                'name': 'PreferredName'
            },
            {
                'name': 'CountryCode'
            },
            {
                'name': 'Zip'
            },
            {
                'name': 'State'
            },
            {
                'name': 'City'
            },
            {
                'name': 'Address1'
            },
            {
                'name': 'Address2'
            },
            {
                'name': 'MobilePhone'
            },
            {
                'name': 'HomePhone'
            },
            {
                'name': 'Gender'
            },
            {
                'name': 'Ethnicity'
            },
            {
                'name': 'VeteranStatus'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'JobTitle'
            },
            {
                'name': 'DepartmentCode'
            },
            {
                'name': 'Disability'
            },
            {
                'name': 'BaseSalary'
            },
            {
                'name': 'SalaryFrequency'
            },
            {
                'name': 'WorkLocationId'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/onboardingemployees-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/payrates-POST': {
        'parameters': [
            {
                'name': 'EffectiveStartDate'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'EffectiveEndDate'
            },
            {
                'name': 'PayRate'
            },
            {
                'name': 'AnnualPayRate'
            },
            {
                'name': 'Type'
            },
            {
                'name': 'Reason'
            },
            {
                'name': 'Notes'
            },
        ]
    },
    '/v1/employees/{employeeId}/payrates-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/payrates/{payrateId}-PUT': {
        'parameters': [
            {
                'name': 'EffectiveStartDate'
            },
            {
                'name': 'PayRate'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'payrateId'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'AnnualPayRate'
            },
            {
                'name': 'Type'
            },
            {
                'name': 'Reason'
            },
            {
                'name': 'Notes'
            },
        ]
    },
    '/v1/employees/{employeeId}/payschedule-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'periodStartDate'
            },
            {
                'name': 'periodEndDate'
            },
            {
                'name': 'continuationToken'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/v1/employees/{employeeId}/paystubs-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'checkDate'
            },
            {
                'name': 'processDate'
            },
            {
                'name': 'plannerId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/paystubs-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'checkDate'
            },
            {
                'name': 'processDate'
            },
            {
                'name': 'plannerId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/paystubsytd-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'toCheckDate'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/paystubsytd-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'toCheckDate'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/payrollhours-POST': {
        'parameters': [
            {
                'name': 'IntegrationVendor'
            },
            {
                'name': 'ProcessId'
            },
            {
                'name': 'ImportEmployees'
            },
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'replaceData'
            },
            {
                'name': 'appendData'
            },
        ]
    },
    '/v1/employees/{employeeId}/payrollhours-POST': {
        'parameters': [
            {
                'name': 'IntegrationVendor'
            },
            {
                'name': 'ProcessId'
            },
            {
                'name': 'EmployeeNumber'
            },
            {
                'name': 'DepartmentCode'
            },
            {
                'name': 'TimeCardData'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'AppId'
            },
            {
                'name': 'LegalEntityId'
            },
            {
                'name': 'JobCode'
            },
        ]
    },
    '/v1/employees/{employeeId}/taxes-POST': {
        'parameters': [
            {
                'name': 'LegalEntityTaxId'
            },
            {
                'name': 'ReciprocityType'
            },
            {
                'name': 'WithholdingEffectiveStartDate'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'FilingStatus'
            },
            {
                'name': 'BlockDate'
            },
            {
                'name': 'NonResidentAlien'
            },
            {
                'name': 'IsProbationaryEmployee'
            },
            {
                'name': 'OccupationalCode'
            },
            {
                'name': 'GeographicCode'
            },
            {
                'name': 'SOCCode'
            },
            {
                'name': 'SeasonalCode'
            },
            {
                'name': 'CountyCode'
            },
            {
                'name': 'SpouseWork'
            },
            {
                'name': 'DependentInsuranceEligible'
            },
            {
                'name': 'DependentInsuranceEligibleDate'
            },
            {
                'name': 'ApplicableBirthyear'
            },
            {
                'name': 'AdjustWithholding'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'Percentage'
            },
            {
                'name': 'NCCICode'
            },
            {
                'name': 'PsdCode'
            },
            {
                'name': 'PsdRate'
            },
            {
                'name': 'OnHold'
            },
            {
                'name': 'Exemptions'
            },
            {
                'name': 'TaxCredit'
            },
        ]
    },
    '/v1/employees/{employeeId}/taxes-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/taxes/filingStatus/{taxCode}-GET': {
        'parameters': [
            {
                'name': 'taxCode'
            },
        ]
    },
    '/v1/employees/taxes/taxFields/{taxCode}-GET': {
        'parameters': [
            {
                'name': 'taxCode'
            },
        ]
    },
    '/v1/employees/{employeeId}/taxes-PUT': {
        'parameters': [
            {
                'name': 'Id'
            },
            {
                'name': 'LegalEntityTaxId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'ReciprocityType'
            },
            {
                'name': 'FilingStatus'
            },
            {
                'name': 'WithholdingEffectiveStartDate'
            },
            {
                'name': 'BlockDate'
            },
            {
                'name': 'NonResidentAlien'
            },
            {
                'name': 'IsProbationaryEmployee'
            },
            {
                'name': 'OccupationalCode'
            },
            {
                'name': 'GeographicCode'
            },
            {
                'name': 'SOCCode'
            },
            {
                'name': 'SeasonalCode'
            },
            {
                'name': 'CountyCode'
            },
            {
                'name': 'SpouseWork'
            },
            {
                'name': 'DependentInsuranceEligible'
            },
            {
                'name': 'DependentInsuranceEligibleDate'
            },
            {
                'name': 'ApplicableBirthyear'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'Percentage'
            },
            {
                'name': 'NCCICode'
            },
            {
                'name': 'PsdCode'
            },
            {
                'name': 'PsdRate'
            },
            {
                'name': 'OnHold'
            },
            {
                'name': 'Exemptions'
            },
            {
                'name': 'TaxCredit'
            },
        ]
    },
    '/v1/employees/{employeeId}/punches-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalEntities/{legalEntityId}/punches-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/timeoffaccruals-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/timeoffaccruals-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees-POST': {
        'parameters': [
            {
                'name': 'LegalEntityId'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'HireDate'
            },
            {
                'name': 'Status'
            },
            {
                'name': 'PaygroupDescription'
            },
            {
                'name': 'DepartmentCode'
            },
            {
                'name': 'PrimaryAddress'
            },
            {
                'name': 'EmployeeNumber'
            },
            {
                'name': 'AlternateEmployeeNumber'
            },
            {
                'name': 'Prefix'
            },
            {
                'name': 'MiddleName'
            },
            {
                'name': 'Suffix'
            },
            {
                'name': 'HomeEmail'
            },
            {
                'name': 'WorkEmail'
            },
            {
                'name': 'Phones'
            },
            {
                'name': 'SocialSecurityNumber'
            },
            {
                'name': 'BirthDate'
            },
            {
                'name': 'Gender'
            },
            {
                'name': 'Ethnicity'
            },
            {
                'name': 'MaritalStatus'
            },
            {
                'name': 'WorkLocation'
            },
            {
                'name': 'JobTitle'
            },
            {
                'name': 'ReHireDate'
            },
            {
                'name': 'Flsa'
            },
            {
                'name': 'Type'
            },
            {
                'name': 'ManagerEmpId'
            },
            {
                'name': 'Veteran'
            },
            {
                'name': 'Disability'
            },
        ]
    },
    '/v1/employees/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'emailType'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/employeesIdentifyingData-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/employees-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'emailType'
            },
            {
                'name': 'statusFilter'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'departmentCode'
            },
            {
                'name': 'workLocationName'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/tenants/{tenantId}/employees-GET': {
        'parameters': [
            {
                'name': 'tenantId'
            },
            {
                'name': 'statusFilter'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'departmentCode'
            },
            {
                'name': 'workLocationName'
            },
            {
                'name': 'jobCode'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'HomeEmail'
            },
            {
                'name': 'WorkEmail'
            },
            {
                'name': 'Phones'
            },
            {
                'name': 'PrimaryAddress'
            },
        ]
    },
    '/v1/employees/{employeeId}/Paygroup-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'payGroupId'
            },
        ]
    },
    '/v1/employees/{employeeId}/identifyingdata-PUT': {
        'parameters': [
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'Suffix'
            },
            {
                'name': 'SocialSecurityNumber'
            },
            {
                'name': 'BirthDate'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'MiddleName'
            },
        ]
    },
    '/v1/employees/{employeeId}/positionandstatus-PUT': {
        'parameters': [
            {
                'name': 'EmploymentStatus'
            },
            {
                'name': 'RehireDate'
            },
            {
                'name': 'EmploymentType'
            },
            {
                'name': 'WorkLocation'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'JobTitle'
            },
            {
                'name': 'Flsa'
            },
            {
                'name': 'ManagerId'
            },
            {
                'name': 'DepartmentId'
            },
        ]
    },
    '/v1/employees/{employeeId}/position-PUT': {
        'parameters': [
            {
                'name': 'EmploymentType'
            },
            {
                'name': 'WorkLocation'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'JobTitle'
            },
            {
                'name': 'Flsa'
            },
            {
                'name': 'ManagerId'
            },
            {
                'name': 'DepartmentId'
            },
        ]
    },
    '/v1/employees/{employeeId}/status-PUT': {
        'parameters': [
            {
                'name': 'EffectiveDate'
            },
            {
                'name': 'EmployeeStatus'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'EmployeeStatusReasonId'
            },
            {
                'name': 'EligibleForRehire'
            },
            {
                'name': 'IsVoluntaryByEmployee'
            },
            {
                'name': 'Notes'
            },
        ]
    },
    '/v1/events/mockevent-POST': {
        'parameters': [
            {
                'name': 'ApplicationId'
            },
            {
                'name': 'NotificationURL'
            },
            {
                'name': 'NotificationSecret'
            },
            {
                'name': 'EventType'
            },
            {
                'name': 'TenantId'
            },
            {
                'name': 'ItemId'
            },
            {
                'name': 'LegalEntityId'
            },
        ]
    },
    '/v1/generalledger/legalentities/{legalEntityId}-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'plannerId'
            },
            {
                'name': 'reportType'
            },
            {
                'name': 'include'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/generalledger/jobcosting/legalentities/{legalEntityId}-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'plannerId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/tenants/{tenantId}/jobtitles-GET': {
        'parameters': [
            {
                'name': 'tenantId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/laborcategories-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/laborcodes-POST': {
        'parameters': [
            {
                'name': 'LaborCategoryId'
            },
            {
                'name': 'LaborCodeName'
            },
            {
                'name': 'Code'
            },
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'EffectiveStartDate'
            },
            {
                'name': 'EffectiveEndDate'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/laborcodes-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/laborcodes-PUT': {
        'parameters': [
            {
                'name': 'LaborCodeId'
            },
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'LaborCodeName'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'Code'
            },
            {
                'name': 'EffectiveStartDate'
            },
            {
                'name': 'EffectiveEndDate'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/v1/legalentities/ActivatedLegalEntityTenantList-GET': {
        'parameters': [
        ]
    },
    '/v1/legalentities/{legalEntityId}/activitytypes-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/certifications-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/certificationOrganizations-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/deductions-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/departments-POST': {
        'parameters': [
            {
                'name': 'Code'
            },
            {
                'name': 'ParentId'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'WorkLocationId'
            },
            {
                'name': 'legalEntityId'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/departments/{departmentId}-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'departmentId'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/departments-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/departments-PUT': {
        'parameters': [
            {
                'name': 'DepartmentId'
            },
            {
                'name': 'Code'
            },
            {
                'name': 'ParentId'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'WorkLocationId'
            },
            {
                'name': 'legalEntityId'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/earnings-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/jobtitles-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/paydata-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'fromCheckDate'
            },
            {
                'name': 'toCheckDate'
            },
            {
                'name': 'processDate'
            },
            {
                'name': 'plannerId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/payGroups-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/payschedule-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'payGroupId'
            },
            {
                'name': 'asOfDate'
            },
            {
                'name': 'untilDate'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/payrollProcessing-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'fromCheckDate'
            },
            {
                'name': 'toCheckDate'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/schedulegroups-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/services-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/statusReasons/{statusCategory}-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'statusCategory'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/timeoffRequestserrorlog/{trackingId}-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'trackingId'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/timeofftypes-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/worklocations-POST': {
        'parameters': [
            {
                'name': 'Name'
            },
            {
                'name': 'Addresses'
            },
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'StoreId'
            },
            {
                'name': 'IsFmlaEligible'
            },
            {
                'name': 'PhoneNumbers'
            },
            {
                'name': 'addressData'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/worklocations/{workLocationId}-DELETE': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'workLocationId'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/worklocations/{workLocationId}-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'workLocationId'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/worklocations-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/worklocations-PUT': {
        'parameters': [
            {
                'name': 'Id'
            },
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'Addresses'
            },
            {
                'name': 'PhoneNumbers'
            },
            {
                'name': 'TimeZone'
            },
            {
                'name': 'IsFmlaEligible'
            },
            {
                'name': 'IsDefault'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/worksites-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/employees/{employeeId}/person-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/v1/tenants/{tenantId}/persons/{personId}-GET': {
        'parameters': [
            {
                'name': 'tenantId'
            },
            {
                'name': 'personId'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/v1/legalEntities/{legalEntityId}/persons-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'include'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/tenants/{tenantId}/persons-GET': {
        'parameters': [
            {
                'name': 'tenantId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/tenants/{tenantId}-GET': {
        'parameters': [
            {
                'name': 'tenantId'
            },
        ]
    },
    '/v1/tenants/{tenantId}/worklocations-GET': {
        'parameters': [
            {
                'name': 'tenantId'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/timeoffRequests/{timeoffRequestId}-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'timeoffRequestId'
            },
        ]
    },
    '/v1/employees/{employeeId}/timeoffrequests-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
    '/v1/legalentities/{legalEntityId}/timeoffrequests-GET': {
        'parameters': [
            {
                'name': 'legalEntityId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'continuationToken'
            },
        ]
    },
};