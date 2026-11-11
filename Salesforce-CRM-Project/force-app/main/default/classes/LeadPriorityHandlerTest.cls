@isTest
public class LeadPriorityHandlerTest {

    @isTest
    static void testLeadPriority() {

        List<Lead> leads = new List<Lead>();

        leads.add(new Lead(
            LastName = 'Test Qualified',
            Company = 'ABC',
            Status = 'Qualified'
        ));

        leads.add(new Lead(
            LastName = 'Test Working',
            Company = 'XYZ',
            Status = 'Working - Contacted'
        ));

        leads.add(new Lead(
            LastName = 'Test New',
            Company = 'PQR',
            Status = 'New'
        ));

        Test.startTest();
        insert leads;
        Test.stopTest();

        List<Lead> results = [
            SELECT Rating, Status
            FROM Lead
            WHERE LastName LIKE 'Test%'
        ];

        System.assertEquals(3, results.size());
    }
}