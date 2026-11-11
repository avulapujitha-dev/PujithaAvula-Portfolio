public with sharing class LeadPriorityHandler {

    public static void updateLeadRating(List<Lead> leads) {

        for (Lead ld : leads) {

            if (ld.Status == 'Qualified') {
                ld.Rating = 'Hot';
            }
            else if (ld.Status == 'Working - Contacted') {
                ld.Rating = 'Warm';
            }
            else {
                ld.Rating = 'Cold';
            }
        }
    }
}