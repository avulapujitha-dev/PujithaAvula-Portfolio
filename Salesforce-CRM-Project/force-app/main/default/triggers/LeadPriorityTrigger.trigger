trigger LeadPriorityTrigger on Lead (before insert, before update) {

    LeadPriorityHandler.updateLeadRating(Trigger.new);

}