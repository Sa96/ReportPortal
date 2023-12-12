# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brandmaster(models.Model):
    brandid = models.FloatField(db_column='BrandId', blank=True, null=True)  # Field name made lowercase.
    brandname = models.TextField(db_column='BrandName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BrandMaster'


class Brcditems(models.Model):
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BrcdItems'


class Cardmaster(models.Model):
    cardid = models.FloatField(db_column='CardId', blank=True, null=True)  # Field name made lowercase.
    cardname = models.TextField(db_column='CardName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CardMaster'


class Cashdrawertrans(models.Model):
    openid = models.FloatField(db_column='OpenId', blank=True, null=True)  # Field name made lowercase.
    opendate = models.DateTimeField(db_column='OpenDate', blank=True, null=True)  # Field name made lowercase.
    opentime = models.CharField(db_column='OpenTime', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    staffid = models.FloatField(db_column='StaffId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CashDrawerTrans'


class Cashtrans(models.Model):
    transid = models.FloatField(db_column='TransId', blank=True, null=True)  # Field name made lowercase.
    invno = models.FloatField(db_column='InvNo', blank=True, null=True)  # Field name made lowercase.
    invno1 = models.CharField(db_column='InvNo1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    transdate = models.DateTimeField(db_column='TransDate', blank=True, null=True)  # Field name made lowercase.
    custid = models.FloatField(db_column='CustId', blank=True, null=True)  # Field name made lowercase.
    cashamt = models.FloatField(db_column='CashAmt', blank=True, null=True)  # Field name made lowercase.
    crcardamt = models.FloatField(db_column='CrCardAmt', blank=True, null=True)  # Field name made lowercase.
    vouchamt = models.FloatField(db_column='VouchAmt', blank=True, null=True)  # Field name made lowercase.
    cardid = models.FloatField(db_column='CardId', blank=True, null=True)  # Field name made lowercase.
    transtype = models.CharField(db_column='TransType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    transamt = models.FloatField(db_column='TransAmt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CashTrans'


class Chequelist(models.Model):
    transid = models.FloatField(db_column='TransId', blank=True, null=True)  # Field name made lowercase.
    transdate = models.DateTimeField(db_column='TransDate', blank=True, null=True)  # Field name made lowercase.
    refno = models.FloatField(db_column='RefNo', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(db_column='RefDate', blank=True, null=True)  # Field name made lowercase.
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    chequeno = models.TextField(db_column='ChequeNo', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chequedate = models.DateTimeField(db_column='ChequeDate', blank=True, null=True)  # Field name made lowercase.
    issuedate = models.DateTimeField(db_column='IssueDate', blank=True, null=True)  # Field name made lowercase.
    chequeamt = models.FloatField(db_column='ChequeAmt', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChequeList'


class Colormaster(models.Model):
    colorid = models.FloatField(db_column='ColorId', blank=True, null=True)  # Field name made lowercase.
    colorname = models.TextField(db_column='ColorName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ColorMaster'


class Countermaster(models.Model):
    type = models.FloatField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CounterMaster'


class Countermedical(models.Model):
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CounterMedical'


class Creditsettlemain(models.Model):
    refno = models.FloatField(db_column='RefNo', blank=True, null=True)  # Field name made lowercase.
    refno1 = models.CharField(db_column='RefNo1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(db_column='RefDate', blank=True, null=True)  # Field name made lowercase.
    custid = models.FloatField(db_column='CustId', blank=True, null=True)  # Field name made lowercase.
    settleamount = models.FloatField(db_column='SettleAmount', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    crdate = models.DateTimeField(db_column='CrDate', blank=True, null=True)  # Field name made lowercase.
    crid = models.FloatField(db_column='CrId', blank=True, null=True)  # Field name made lowercase.
    saleid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CreditSettleMain'


class Creditsettlesub(models.Model):
    refno = models.FloatField(db_column='RefNo', blank=True, null=True)  # Field name made lowercase.
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    invid1 = models.CharField(db_column='InvId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    invamt = models.FloatField(db_column='InvAmt', blank=True, null=True)  # Field name made lowercase.
    paidamt = models.FloatField(db_column='PaidAmt', blank=True, null=True)  # Field name made lowercase.
    balamt = models.FloatField(db_column='BalAmt', blank=True, null=True)  # Field name made lowercase.
    recamt = models.FloatField(db_column='RecAmt', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.
    cardamt = models.FloatField(db_column='CardAmt', blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.FloatField(db_column='DeliveryStatus', blank=True, null=True)  # Field name made lowercase.
    cardid = models.FloatField(db_column='CardId', blank=True, null=True)  # Field name made lowercase.
    shiftid = models.FloatField(db_column='ShiftId', blank=True, null=True)  # Field name made lowercase.
    saleid = models.FloatField(db_column='SaleId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditSettleSub'


class Credittrans(models.Model):
    transid = models.FloatField(db_column='TransId', blank=True, null=True)  # Field name made lowercase.
    refid = models.FloatField(db_column='RefId', blank=True, null=True)  # Field name made lowercase.
    refid1 = models.CharField(db_column='RefId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(db_column='RefDate', blank=True, null=True)  # Field name made lowercase.
    custid = models.FloatField(db_column='CustId', blank=True, null=True)  # Field name made lowercase.
    creditamt = models.FloatField(db_column='CreditAmt', blank=True, null=True)  # Field name made lowercase.
    debitamt = models.FloatField(db_column='DebitAmt', blank=True, null=True)  # Field name made lowercase.
    transtype = models.CharField(db_column='TransType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    debitamtcard = models.FloatField(db_column='DebitAmtCard', blank=True, null=True)  # Field name made lowercase.
    cid = models.FloatField(db_column='Cid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditTrans'


class Currencymaster(models.Model):
    currencyid = models.FloatField(db_column='CurrencyId', blank=True, null=True)  # Field name made lowercase.
    currencyname = models.TextField(db_column='CurrencyName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    exgrate = models.FloatField(db_column='ExgRate', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CurrencyMaster'


class Customergroupdiscount(models.Model):
    custid = models.FloatField(db_column='CustId', blank=True, null=True)  # Field name made lowercase.
    subgroupid = models.FloatField(db_column='SubGroupId', blank=True, null=True)  # Field name made lowercase.
    discper = models.FloatField(db_column='DiscPer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerGroupDiscount'


class Customermaster(models.Model):
    custid = models.FloatField(db_column='CustId', blank=True, primary_key=True)  # Field name made lowercase.
    custname = models.TextField(db_column='CustName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    add1 = models.TextField(db_column='Add1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    add2 = models.TextField(db_column='Add2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    add3 = models.TextField(db_column='Add3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telephoneno = models.CharField(db_column='TelephoneNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    faxno = models.CharField(db_column='FaxNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailid = models.TextField(db_column='EmailId', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    crdate = models.DateTimeField(db_column='CrDate', blank=True, null=True)  # Field name made lowercase.
    crid = models.FloatField(db_column='CrId', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.FloatField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    birthmonthid = models.FloatField(db_column='BirthMonthId', blank=True, null=True)  # Field name made lowercase.
    discper = models.FloatField(db_column='DiscPer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerMaster'


class Dayendpassword(models.Model):
    pswd = models.CharField(db_column='Pswd', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DayEndPassword'


class Daytrans(models.Model):
    saledate = models.DateTimeField(db_column='SaleDate', blank=True, null=True)  # Field name made lowercase.
    cashpuramt = models.FloatField(db_column='CashPurAmt', blank=True, null=True)  # Field name made lowercase.
    creditpuramt = models.FloatField(db_column='CreditPurAmt', blank=True, null=True)  # Field name made lowercase.
    bankamt = models.FloatField(db_column='BankAmt', blank=True, null=True)  # Field name made lowercase.
    expamt = models.FloatField(db_column='ExpAmt', blank=True, null=True)  # Field name made lowercase.
    sales = models.FloatField(db_column='Sales', blank=True, null=True)  # Field name made lowercase.
    cardsales = models.FloatField(db_column='CardSales', blank=True, null=True)  # Field name made lowercase.
    tillcash = models.FloatField(db_column='TillCash', blank=True, null=True)  # Field name made lowercase.
    netcash = models.FloatField(db_column='NetCash', blank=True, null=True)  # Field name made lowercase.
    diffcash = models.FloatField(db_column='DiffCash', blank=True, null=True)  # Field name made lowercase.
    ocashpuramt = models.FloatField(db_column='OCashPurAmt', blank=True, null=True)  # Field name made lowercase.
    ocreditpuramt = models.FloatField(db_column='OCreditPurAmt', blank=True, null=True)  # Field name made lowercase.
    obankamt = models.FloatField(db_column='OBankAmt', blank=True, null=True)  # Field name made lowercase.
    oexpamt = models.FloatField(db_column='OExpAmt', blank=True, null=True)  # Field name made lowercase.
    osales = models.FloatField(db_column='OSales', blank=True, null=True)  # Field name made lowercase.
    tcashpur = models.FloatField(db_column='TCashPur', blank=True, null=True)  # Field name made lowercase.
    tcreditpur = models.FloatField(db_column='TCreditPur', blank=True, null=True)  # Field name made lowercase.
    tbank = models.FloatField(db_column='TBank', blank=True, null=True)  # Field name made lowercase.
    texp = models.FloatField(db_column='TExp', blank=True, null=True)  # Field name made lowercase.
    tsales = models.FloatField(db_column='TSales', blank=True, null=True)  # Field name made lowercase.
    ocardsales = models.FloatField(db_column='OCardSales', blank=True, null=True)  # Field name made lowercase.
    tcardsales = models.FloatField(db_column='TCardSales', blank=True, null=True)  # Field name made lowercase.
    ocashsales = models.FloatField(db_column='OCashSales', blank=True, null=True)  # Field name made lowercase.
    cashsales = models.FloatField(db_column='CashSales', blank=True, null=True)  # Field name made lowercase.
    tcashsales = models.FloatField(db_column='TCashSales', blank=True, null=True)  # Field name made lowercase.
    creditsales = models.FloatField(db_column='CreditSales', blank=True, null=True)  # Field name made lowercase.
    creditreceived = models.FloatField(db_column='CreditReceived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DayTrans'


class Discountmaster(models.Model):
    discountid = models.FloatField(db_column='DiscountId', blank=True, null=True)  # Field name made lowercase.
    discount = models.FloatField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiscountMaster'


class Expgroupmaster(models.Model):
    expgroupid = models.FloatField(db_column='ExpGroupId', blank=True, null=True)  # Field name made lowercase.
    expgroupname = models.TextField(db_column='ExpGroupName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExpGroupMaster'


class Expsubgroupmaster(models.Model):
    expsubgroupid = models.FloatField(db_column='ExpSubGroupId', blank=True, null=True)  # Field name made lowercase.
    expgroupid = models.FloatField(db_column='ExpGroupId', blank=True, null=True)  # Field name made lowercase.
    expsubgroupname = models.TextField(db_column='ExpSubGroupName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExpSubGroupMaster'


class Expenseentry(models.Model):
    expid = models.FloatField(db_column='ExpId', blank=True, null=True)  # Field name made lowercase.
    expid1 = models.CharField(db_column='ExpId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    expdate = models.DateTimeField(db_column='ExpDate', blank=True, null=True)  # Field name made lowercase.
    expgroupid = models.FloatField(db_column='ExpGroupId', blank=True, null=True)  # Field name made lowercase.
    expsubgroupid = models.FloatField(db_column='ExpSubGroupId', blank=True, null=True)  # Field name made lowercase.
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    trn = models.CharField(db_column='TRN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    refno = models.TextField(db_column='RefNo', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    expamt = models.FloatField(db_column='ExpAmt', blank=True, null=True)  # Field name made lowercase.
    vatamt = models.FloatField(db_column='VatAmt', blank=True, null=True)  # Field name made lowercase.
    totalamt = models.FloatField(db_column='TotalAmt', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vattype = models.FloatField(db_column='VatType', blank=True, null=True)  # Field name made lowercase.
    paytype = models.FloatField(db_column='PayType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExpenseEntry'


class Finishmaster(models.Model):
    finishid = models.FloatField(db_column='FinishId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinishMaster'


class Frommailmaster(models.Model):
    mailid = models.TextField(db_column='MailId', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mailpswd = models.TextField(db_column='MailPswd', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FromMailMaster'


class Generalsettings(models.Model):
    head1 = models.TextField(db_column='Head1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    head2 = models.TextField(db_column='Head2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    head3 = models.TextField(db_column='Head3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    head4 = models.TextField(db_column='Head4', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    portname = models.CharField(db_column='PortName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    customerdisplay = models.FloatField(db_column='CustomerDisplay', blank=True, null=True)  # Field name made lowercase.
    invprinter = models.CharField(db_column='InvPrinter', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    loccode = models.CharField(db_column='LocCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doccode = models.CharField(db_column='DocCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    footer1 = models.TextField(db_column='Footer1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    footer2 = models.TextField(db_column='Footer2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    footer3 = models.TextField(db_column='Footer3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    footer4 = models.TextField(db_column='Footer4', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baudrate = models.FloatField(db_column='BaudRate', blank=True, null=True)  # Field name made lowercase.
    polemsg1 = models.TextField(db_column='PoleMsg1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    polemsg2 = models.TextField(db_column='PoleMsg2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    logo = models.FloatField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    logox = models.FloatField(db_column='LogoX', blank=True, null=True)  # Field name made lowercase.
    logoy = models.FloatField(db_column='LogoY', blank=True, null=True)  # Field name made lowercase.
    head5 = models.TextField(db_column='Head5', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kprinter1 = models.TextField(db_column='KPrinter1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kprinter2 = models.TextField(db_column='KPrinter2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kprinter3 = models.TextField(db_column='KPrinter3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kprinter4 = models.TextField(db_column='KPrinter4', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tabprinter = models.TextField(db_column='TabPrinter', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricechange = models.IntegerField(db_column='PriceChange', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeneralSettings'


class Groupmaster(models.Model):
    groupid = models.FloatField(db_column='GroupId', blank=True, null=True)  # Field name made lowercase.
    groupname = models.TextField(db_column='GroupName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupMaster'


class Insurancemaster(models.Model):
    insuid = models.FloatField(db_column='InsuId', blank=True, null=True)  # Field name made lowercase.
    insuname = models.TextField(db_column='InsuName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InsuranceMaster'


class Invoicemain(models.Model):
    invid = models.FloatField(db_column='InvId', blank=True, primary_key=True)  # Field name made lowercase.
    invid1 = models.CharField(db_column='InvId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    invtime = models.CharField(db_column='InvTime', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    settletime = models.CharField(db_column='SettleTime', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    settledate = models.DateTimeField(db_column='SettleDate', blank=True, null=True)  # Field name made lowercase.
    custid = models.FloatField(db_column='CustId', blank=True, null=True)  # Field name made lowercase.
    totamt = models.FloatField(db_column='TotAmt', blank=True, null=True)  # Field name made lowercase.
    itemdiscamt = models.FloatField(db_column='ItemDiscAmt', blank=True, null=True)  # Field name made lowercase.
    invoicediscamt = models.FloatField(db_column='InvoiceDiscAmt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    advanceamt = models.FloatField(db_column='AdvanceAmt', blank=True, null=True)  # Field name made lowercase.
    cardadvanceamt = models.FloatField(db_column='CardAdvanceAmt', blank=True, null=True)  # Field name made lowercase.
    cashamt = models.FloatField(db_column='CashAmt', blank=True, null=True)  # Field name made lowercase.
    crcardamt = models.FloatField(db_column='CrCardAmt', blank=True, null=True)  # Field name made lowercase.
    creditamt = models.FloatField(db_column='CreditAmt', blank=True, null=True)  # Field name made lowercase.
    vouchamt = models.FloatField(db_column='VouchAmt', blank=True, null=True)  # Field name made lowercase.
    changeamt = models.FloatField(db_column='ChangeAmt', blank=True, null=True)  # Field name made lowercase.
    totcostamt = models.FloatField(db_column='TotCostAmt', blank=True, null=True)  # Field name made lowercase.
    netprofitamt = models.FloatField(db_column='NetProfitAmt', blank=True, null=True)  # Field name made lowercase.
    userid = models.FloatField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    invoicetype = models.FloatField(db_column='InvoiceType', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cancelstatus = models.FloatField(db_column='CancelStatus', blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.FloatField(db_column='DeliveryStatus', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    deliveryremarks = models.TextField(db_column='DeliveryRemarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rsph = models.CharField(db_column='RSph', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rcyl = models.CharField(db_column='RCyl', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    raxis = models.CharField(db_column='RAxis', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    radd = models.CharField(db_column='RAdd', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lsph = models.CharField(db_column='LSph', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lcyl = models.CharField(db_column='LCyl', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    laxis = models.CharField(db_column='LAxis', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ladd = models.CharField(db_column='LAdd', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardid = models.FloatField(db_column='CardId', blank=True, null=True)  # Field name made lowercase.
    vouchid = models.FloatField(db_column='VouchId', blank=True, null=True)  # Field name made lowercase.
    ipdr = models.CharField(db_column='IPDR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ipdl = models.CharField(db_column='IPDL', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stfid = models.FloatField(db_column='sTFID', blank=True, null=True)  # Field name made lowercase.
    advcredit = models.FloatField(db_column='aDVcREDIT', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(blank=True, null=True)
    settlestatus = models.FloatField(blank=True, null=True)
    insuamt = models.FloatField(db_column='InsuAmt', blank=True, null=True)  # Field name made lowercase.
    insuid = models.FloatField(db_column='InsuId', blank=True, null=True)  # Field name made lowercase.
    medicalremarks = models.TextField(db_column='MedicalRemarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saleid = models.FloatField(db_column='SaleId', blank=True, null=True)  # Field name made lowercase.
    typeid = models.FloatField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    receivedamt = models.FloatField(db_column='ReceivedAmt', blank=True, null=True)  # Field name made lowercase.
    fromid = models.FloatField(db_column='FromId', blank=True, null=True)  # Field name made lowercase.
    toid = models.FloatField(db_column='ToId', blank=True, null=True)  # Field name made lowercase.
    reasonid = models.FloatField(db_column='ReasonId', blank=True, null=True)  # Field name made lowercase.
    returnamt = models.FloatField(db_column='ReturnAmt', blank=True, null=True)  # Field name made lowercase.
    transid = models.FloatField(db_column='TransId', blank=True, null=True)  # Field name made lowercase.
    vatamount = models.FloatField(db_column='VatAmount', blank=True, null=True)  # Field name made lowercase.
    grandtotal = models.FloatField(db_column='GrandTotal', blank=True, null=True)  # Field name made lowercase.
    pendingstatus = models.FloatField(db_column='PendingStatus', blank=True, null=True)  # Field name made lowercase.
    tableid = models.FloatField(db_column='TableId', blank=True, null=True)  # Field name made lowercase.
    ordertype = models.FloatField(db_column='OrderType', blank=True, null=True)  # Field name made lowercase.
    onlineid = models.FloatField(db_column='OnlineId', blank=True, null=True)  # Field name made lowercase.
    counterid = models.FloatField(db_column='CounterId', blank=True, null=True)  # Field name made lowercase.
    korderno = models.FloatField(db_column='KOrderNo', blank=True, null=True)  # Field name made lowercase.
    pax = models.FloatField(db_column='Pax', blank=True, null=True)  # Field name made lowercase.
    pickuptime = models.CharField(db_column='PickUpTime', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    timeid = models.FloatField(db_column='TimeID', blank=True, null=True)  # Field name made lowercase.
    settletimeid = models.FloatField(db_column='SettleTimeID', blank=True, null=True)  # Field name made lowercase.
    postingstatus = models.FloatField(db_column='PostingStatus', blank=True, null=True)  # Field name made lowercase.
    shiftid = models.FloatField(db_column='ShiftId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceMain'


class Invoicesub(models.Model):
    invid = models.FloatField(db_column='InvId', blank=True, primary_key=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    totamt = models.FloatField(db_column='TotAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    costprice = models.FloatField(db_column='CostPrice', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo')  # Field name made lowercase.
    docno = models.FloatField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    locname = models.TextField(db_column='LocName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    korderno = models.FloatField(db_column='KOrderNo', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    kitchenid = models.FloatField(db_column='KitchenId', blank=True, null=True)  # Field name made lowercase.
    kotnotes = models.CharField(db_column='KOTNotes', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postingstatus = models.FloatField(db_column='PostingStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceSub'


class Invoicetime(models.Model):
    timeid = models.FloatField(db_column='TimeID', blank=True, null=True)  # Field name made lowercase.
    time_name = models.TextField(db_column='Time_Name', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceTime'


class Itemmaster(models.Model):
    itemid = models.FloatField(db_column='ItemId', blank=True, primary_key=True)  # Field name made lowercase.
    itemid1 = models.CharField(db_column='ItemId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemname = models.TextField(db_column='ItemName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.TextField(db_column='ItemCode', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    suppr = models.FloatField(db_column='SupPr', blank=True, null=True)  # Field name made lowercase.
    disc = models.FloatField(db_column='Disc', blank=True, null=True)  # Field name made lowercase.
    costprice = models.FloatField(db_column='CostPrice', blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.FloatField(db_column='SellingPrice', blank=True, null=True)  # Field name made lowercase.
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    groupid = models.FloatField(db_column='GroupId', blank=True, null=True)  # Field name made lowercase.
    subgroupid = models.FloatField(db_column='SubGroupId', blank=True, null=True)  # Field name made lowercase.
    colorid = models.FloatField(db_column='ColorId', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.FloatField(db_column='SizeId', blank=True, null=True)  # Field name made lowercase.
    unitid = models.FloatField(db_column='UnitId')  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    counteritem = models.FloatField(db_column='CounterItem', blank=True, null=True)  # Field name made lowercase.
    itemtype = models.FloatField(db_column='ItemType', blank=True, null=True)  # Field name made lowercase.
    snc = models.TextField(db_column='SnC', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    brandid = models.FloatField(db_column='BrandId', blank=True, null=True)  # Field name made lowercase.
    subgroupid2 = models.FloatField(db_column='SubGroupId2', blank=True, null=True)  # Field name made lowercase.
    subgroupid3 = models.FloatField(db_column='SubGroupId3', blank=True, null=True)  # Field name made lowercase.
    styleno = models.TextField(db_column='StyleNo', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    seasoncode = models.TextField(db_column='SeasonCode', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    enableprice = models.FloatField(db_column='EnablePrice', blank=True, null=True)  # Field name made lowercase.
    arabicname = models.TextField(db_column='ArabicName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    color = models.TextField(db_column='Color', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    size = models.TextField(db_column='Size', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sellingprice2 = models.FloatField(db_column='SellingPrice2', blank=True, null=True)  # Field name made lowercase.
    sellingprice3 = models.FloatField(db_column='SellingPrice3', blank=True, null=True)  # Field name made lowercase.
    pricename1 = models.CharField(db_column='PriceName1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename2 = models.CharField(db_column='PriceName2', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename3 = models.CharField(db_column='PriceName3', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kot = models.FloatField(db_column='KOT', blank=True, null=True)  # Field name made lowercase.
    sellingprice4 = models.FloatField(db_column='SellingPrice4', blank=True, null=True)  # Field name made lowercase.
    sellingprice5 = models.FloatField(db_column='SellingPrice5', blank=True, null=True)  # Field name made lowercase.
    sellingprice6 = models.FloatField(db_column='SellingPrice6', blank=True, null=True)  # Field name made lowercase.
    sellingprice7 = models.FloatField(db_column='SellingPrice7', blank=True, null=True)  # Field name made lowercase.
    sellingprice8 = models.FloatField(db_column='SellingPrice8', blank=True, null=True)  # Field name made lowercase.
    pricename4 = models.CharField(db_column='PriceName4', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename5 = models.CharField(db_column='PriceName5', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename6 = models.CharField(db_column='PriceName6', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename7 = models.CharField(db_column='PriceName7', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename8 = models.CharField(db_column='PriceName8', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemMaster'


class Kitchennotes(models.Model):
    id = models.FloatField(db_column='Id', blank=True, primary_key=True)  # Field name made lowercase.
    kotnotes = models.TextField(db_column='KOTNotes', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KitchenNotes'


class Locationmaster(models.Model):
    locid = models.FloatField(db_column='LocId', blank=True, null=True)  # Field name made lowercase.
    locname = models.TextField(db_column='LocName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocationMaster'


class Modules(models.Model):
    modulecode = models.FloatField(db_column='ModuleCode', blank=True, null=True)  # Field name made lowercase.
    modulename = models.TextField(db_column='ModuleName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modules'


class Monthmaster(models.Model):
    monthid = models.FloatField(db_column='MonthId', blank=True, null=True)  # Field name made lowercase.
    monthname = models.TextField(db_column='MonthName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    enddate = models.FloatField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MonthMaster'


class Onlinemaster(models.Model):
    onlineid = models.FloatField(db_column='OnlineId', blank=True, null=True)  # Field name made lowercase.
    onlinename = models.TextField(db_column='OnlineName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    onlinetype = models.FloatField(db_column='OnlineType', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    priceid = models.FloatField(db_column='PriceId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineMaster'


class Onlinesetting(models.Model):
    onlineid1 = models.FloatField(db_column='OnlineId1', blank=True, null=True)  # Field name made lowercase.
    onlineid2 = models.FloatField(db_column='OnlineId2', blank=True, null=True)  # Field name made lowercase.
    onlineid3 = models.FloatField(db_column='OnlineId3', blank=True, null=True)  # Field name made lowercase.
    onlineid4 = models.FloatField(db_column='OnlineId4', blank=True, null=True)  # Field name made lowercase.
    onlineid5 = models.FloatField(db_column='OnlineId5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineSetting'


class Payinout(models.Model):
    payid = models.FloatField(db_column='PayId', blank=True, null=True)  # Field name made lowercase.
    paydate = models.DateTimeField(db_column='PayDate', blank=True, null=True)  # Field name made lowercase.
    saleid = models.FloatField(db_column='SaleId', blank=True, null=True)  # Field name made lowercase.
    saledate = models.DateTimeField(db_column='SaleDate', blank=True, null=True)  # Field name made lowercase.
    payinamt = models.FloatField(db_column='PayInAmt', blank=True, null=True)  # Field name made lowercase.
    payoutamt = models.FloatField(db_column='PayOutAmt', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paytime = models.CharField(db_column='PayTime', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    expid = models.FloatField(db_column='ExpId', blank=True, null=True)  # Field name made lowercase.
    shiftid = models.FloatField(db_column='ShiftId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PayInOut'


class Paymentdetails(models.Model):
    rcpt_dt = models.DateTimeField(db_column='RCPT_DT', blank=True, null=True)  # Field name made lowercase.
    rcpt_num = models.FloatField(db_column='RCPT_NUM', blank=True, null=True)  # Field name made lowercase.
    payment_name = models.CharField(db_column='PAYMENT_NAME', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    currency_code = models.CharField(db_column='CURRENCY_CODE', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    exchange_rate = models.FloatField(db_column='EXCHANGE_RATE', blank=True, null=True)  # Field name made lowercase.
    tender_amount = models.FloatField(db_column='TENDER_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    op_cur = models.CharField(db_column='OP_CUR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bc_exch = models.FloatField(db_column='BC_EXCH', blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='PAYMENT_STATUS', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentDetails'


class Paymentmaster(models.Model):
    payid = models.FloatField(db_column='PayId', blank=True, null=True)  # Field name made lowercase.
    paymode = models.TextField(db_column='PayMode', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentMaster'


class Pendinginvoice(models.Model):
    custid = models.FloatField(db_column='CustId', blank=True, null=True)  # Field name made lowercase.
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PendingInvoice'


class Pendingpurchase(models.Model):
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    purchid = models.FloatField(db_column='PurchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PendingPurchase'


class Physicalstockmain(models.Model):
    phystockid = models.FloatField(db_column='PhyStockId', blank=True, null=True)  # Field name made lowercase.
    phystockid1 = models.CharField(db_column='PhyStockId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phystockdate = models.DateTimeField(db_column='PhyStockDate', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhysicalStockMain'


class Physicalstocksub(models.Model):
    phystockid = models.FloatField(db_column='PhyStockId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    itemid1 = models.CharField(db_column='ItemId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemname = models.TextField(db_column='ItemName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    compqty = models.FloatField(db_column='CompQty', blank=True, null=True)  # Field name made lowercase.
    phyqty = models.FloatField(db_column='PhyQty', blank=True, null=True)  # Field name made lowercase.
    diffqty = models.FloatField(db_column='DiffQty', blank=True, null=True)  # Field name made lowercase.
    addqty = models.FloatField(db_column='AddQty', blank=True, null=True)  # Field name made lowercase.
    redqty = models.FloatField(db_column='RedQty', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhysicalStockSub'


class PostingInvoicemain(models.Model):
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    invid1 = models.CharField(db_column='InvId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    invtime = models.CharField(db_column='InvTime', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    settletime = models.CharField(db_column='SettleTime', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    settledate = models.DateTimeField(db_column='SettleDate', blank=True, null=True)  # Field name made lowercase.
    custid = models.FloatField(db_column='CustId', blank=True, null=True)  # Field name made lowercase.
    totamt = models.FloatField(db_column='TotAmt', blank=True, null=True)  # Field name made lowercase.
    itemdiscamt = models.FloatField(db_column='ItemDiscAmt', blank=True, null=True)  # Field name made lowercase.
    invoicediscamt = models.FloatField(db_column='InvoiceDiscAmt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    advanceamt = models.FloatField(db_column='AdvanceAmt', blank=True, null=True)  # Field name made lowercase.
    cardadvanceamt = models.FloatField(db_column='CardAdvanceAmt', blank=True, null=True)  # Field name made lowercase.
    cashamt = models.FloatField(db_column='CashAmt', blank=True, null=True)  # Field name made lowercase.
    crcardamt = models.FloatField(db_column='CrCardAmt', blank=True, null=True)  # Field name made lowercase.
    creditamt = models.FloatField(db_column='CreditAmt', blank=True, null=True)  # Field name made lowercase.
    vouchamt = models.FloatField(db_column='VouchAmt', blank=True, null=True)  # Field name made lowercase.
    changeamt = models.FloatField(db_column='ChangeAmt', blank=True, null=True)  # Field name made lowercase.
    totcostamt = models.FloatField(db_column='TotCostAmt', blank=True, null=True)  # Field name made lowercase.
    netprofitamt = models.FloatField(db_column='NetProfitAmt', blank=True, null=True)  # Field name made lowercase.
    userid = models.FloatField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    invoicetype = models.FloatField(db_column='InvoiceType', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cancelstatus = models.FloatField(db_column='CancelStatus', blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.FloatField(db_column='DeliveryStatus', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    deliveryremarks = models.TextField(db_column='DeliveryRemarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rsph = models.CharField(db_column='RSph', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rcyl = models.CharField(db_column='RCyl', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    raxis = models.CharField(db_column='RAxis', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    radd = models.CharField(db_column='RAdd', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lsph = models.CharField(db_column='LSph', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lcyl = models.CharField(db_column='LCyl', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    laxis = models.CharField(db_column='LAxis', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ladd = models.CharField(db_column='LAdd', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cardid = models.FloatField(db_column='CardId', blank=True, null=True)  # Field name made lowercase.
    vouchid = models.FloatField(db_column='VouchId', blank=True, null=True)  # Field name made lowercase.
    ipdr = models.CharField(db_column='IPDR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ipdl = models.CharField(db_column='IPDL', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stfid = models.FloatField(db_column='sTFID', blank=True, null=True)  # Field name made lowercase.
    advcredit = models.FloatField(db_column='aDVcREDIT', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(blank=True, null=True)
    settlestatus = models.FloatField(blank=True, null=True)
    insuamt = models.FloatField(db_column='InsuAmt', blank=True, null=True)  # Field name made lowercase.
    insuid = models.FloatField(db_column='InsuId', blank=True, null=True)  # Field name made lowercase.
    medicalremarks = models.TextField(db_column='MedicalRemarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saleid = models.FloatField(db_column='SaleId', blank=True, null=True)  # Field name made lowercase.
    typeid = models.FloatField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    receivedamt = models.FloatField(db_column='ReceivedAmt', blank=True, null=True)  # Field name made lowercase.
    fromid = models.FloatField(db_column='FromId', blank=True, null=True)  # Field name made lowercase.
    toid = models.FloatField(db_column='ToId', blank=True, null=True)  # Field name made lowercase.
    reasonid = models.FloatField(db_column='ReasonId', blank=True, null=True)  # Field name made lowercase.
    returnamt = models.FloatField(db_column='ReturnAmt', blank=True, null=True)  # Field name made lowercase.
    transid = models.FloatField(db_column='TransId', blank=True, null=True)  # Field name made lowercase.
    vatamount = models.FloatField(db_column='VatAmount', blank=True, null=True)  # Field name made lowercase.
    grandtotal = models.FloatField(db_column='GrandTotal', blank=True, null=True)  # Field name made lowercase.
    pendingstatus = models.FloatField(db_column='PendingStatus', blank=True, null=True)  # Field name made lowercase.
    tableid = models.FloatField(db_column='TableId', blank=True, null=True)  # Field name made lowercase.
    ordertype = models.FloatField(db_column='OrderType', blank=True, null=True)  # Field name made lowercase.
    onlineid = models.FloatField(db_column='OnlineId', blank=True, null=True)  # Field name made lowercase.
    counterid = models.FloatField(db_column='CounterId', blank=True, null=True)  # Field name made lowercase.
    korderno = models.FloatField(db_column='KOrderNo', blank=True, null=True)  # Field name made lowercase.
    pax = models.FloatField(db_column='Pax', blank=True, null=True)  # Field name made lowercase.
    pickuptime = models.CharField(db_column='PickUpTime', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    timeid = models.FloatField(db_column='TimeID', blank=True, null=True)  # Field name made lowercase.
    settletimeid = models.FloatField(db_column='SettleTimeID', blank=True, null=True)  # Field name made lowercase.
    postingstatus = models.FloatField(db_column='PostingStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Posting_InvoiceMain'


class PostingInvoicesub(models.Model):
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    totamt = models.FloatField(db_column='TotAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    costprice = models.FloatField(db_column='CostPrice', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo')  # Field name made lowercase.
    docno = models.FloatField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    locname = models.TextField(db_column='LocName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    korderno = models.FloatField(db_column='KOrderNo', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    kitchenid = models.FloatField(db_column='KitchenId', blank=True, null=True)  # Field name made lowercase.
    kotnotes = models.CharField(db_column='KOTNotes', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postingstatus = models.FloatField(db_column='PostingStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Posting_InvoiceSub'


class PostingItemmaster(models.Model):
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    itemid1 = models.CharField(db_column='ItemId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemname = models.TextField(db_column='ItemName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.TextField(db_column='ItemCode', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    suppr = models.FloatField(db_column='SupPr', blank=True, null=True)  # Field name made lowercase.
    disc = models.FloatField(db_column='Disc', blank=True, null=True)  # Field name made lowercase.
    costprice = models.FloatField(db_column='CostPrice', blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.FloatField(db_column='SellingPrice', blank=True, null=True)  # Field name made lowercase.
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    groupid = models.FloatField(db_column='GroupId', blank=True, null=True)  # Field name made lowercase.
    subgroupid = models.FloatField(db_column='SubGroupId', blank=True, null=True)  # Field name made lowercase.
    colorid = models.FloatField(db_column='ColorId', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.FloatField(db_column='SizeId', blank=True, null=True)  # Field name made lowercase.
    unitid = models.FloatField(db_column='UnitId')  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    counteritem = models.FloatField(db_column='CounterItem', blank=True, null=True)  # Field name made lowercase.
    itemtype = models.FloatField(db_column='ItemType', blank=True, null=True)  # Field name made lowercase.
    snc = models.TextField(db_column='SnC', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    brandid = models.FloatField(db_column='BrandId', blank=True, null=True)  # Field name made lowercase.
    subgroupid2 = models.FloatField(db_column='SubGroupId2', blank=True, null=True)  # Field name made lowercase.
    subgroupid3 = models.FloatField(db_column='SubGroupId3', blank=True, null=True)  # Field name made lowercase.
    styleno = models.TextField(db_column='StyleNo', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    seasoncode = models.TextField(db_column='SeasonCode', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    enableprice = models.FloatField(db_column='EnablePrice', blank=True, null=True)  # Field name made lowercase.
    arabicname = models.TextField(db_column='ArabicName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    color = models.TextField(db_column='Color', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    size = models.TextField(db_column='Size', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sellingprice2 = models.FloatField(db_column='SellingPrice2', blank=True, null=True)  # Field name made lowercase.
    sellingprice3 = models.FloatField(db_column='SellingPrice3', blank=True, null=True)  # Field name made lowercase.
    pricename1 = models.CharField(db_column='PriceName1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename2 = models.CharField(db_column='PriceName2', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename3 = models.CharField(db_column='PriceName3', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kot = models.FloatField(db_column='KOT', blank=True, null=True)  # Field name made lowercase.
    sellingprice4 = models.FloatField(db_column='SellingPrice4', blank=True, null=True)  # Field name made lowercase.
    sellingprice5 = models.FloatField(db_column='SellingPrice5', blank=True, null=True)  # Field name made lowercase.
    sellingprice6 = models.FloatField(db_column='SellingPrice6', blank=True, null=True)  # Field name made lowercase.
    sellingprice7 = models.FloatField(db_column='SellingPrice7', blank=True, null=True)  # Field name made lowercase.
    sellingprice8 = models.FloatField(db_column='SellingPrice8', blank=True, null=True)  # Field name made lowercase.
    pricename4 = models.CharField(db_column='PriceName4', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename5 = models.CharField(db_column='PriceName5', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename6 = models.CharField(db_column='PriceName6', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename7 = models.CharField(db_column='PriceName7', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pricename8 = models.CharField(db_column='PriceName8', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Posting_ItemMaster'


class PostingTypetrans(models.Model):
    typeid = models.FloatField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    invno = models.FloatField(db_column='InvNo', blank=True, null=True)  # Field name made lowercase.
    saleid = models.FloatField(db_column='SaleId', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    dhsamt = models.FloatField(db_column='DHSAmt', blank=True, null=True)  # Field name made lowercase.
    postingstatus = models.FloatField(db_column='PostingStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Posting_TypeTrans'


class Promomain(models.Model):
    promoid = models.FloatField(db_column='PromoId', blank=True, null=True)  # Field name made lowercase.
    promoid1 = models.CharField(db_column='PromoId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    promoname = models.TextField(db_column='PromoName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    crdate = models.DateTimeField(db_column='CrDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromoMain'


class Promosub(models.Model):
    promoid = models.FloatField(db_column='PromoId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.FloatField(db_column='SellingPrice', blank=True, null=True)  # Field name made lowercase.
    promoprice = models.FloatField(db_column='PromoPrice', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='Slno', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromoSub'


class Purchasemain(models.Model):
    purchid = models.FloatField(db_column='PurchId', blank=True, null=True)  # Field name made lowercase.
    purchid1 = models.CharField(db_column='PurchId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    purchdate = models.DateTimeField(db_column='PurchDate', blank=True, null=True)  # Field name made lowercase.
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    purchaseamt = models.FloatField(db_column='PurchaseAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.TextField(db_column='InvoiceNo', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vatamt = models.FloatField(db_column='VatAmt', blank=True, null=True)  # Field name made lowercase.
    grandtotal = models.FloatField(db_column='GrandTotal', blank=True, null=True)  # Field name made lowercase.
    trn = models.CharField(db_column='TRN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vatstatus = models.FloatField(db_column='VATStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseMain'


class Purchasereturnmain(models.Model):
    purchretid = models.FloatField(db_column='PurchRetId', blank=True, null=True)  # Field name made lowercase.
    purchretid1 = models.CharField(db_column='PurchRetId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    purchretdate = models.DateTimeField(db_column='PurchRetDate', blank=True, null=True)  # Field name made lowercase.
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    purchretamt = models.FloatField(db_column='PurchRetAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseReturnMain'


class Purchasereturnsub(models.Model):
    purchretid = models.FloatField(db_column='PurchRetId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.FloatField(db_column='SellingPrice', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseReturnSub'


class Purchasesub(models.Model):
    purchid = models.FloatField(db_column='PurchId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.FloatField(db_column='SellingPrice', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseSub'


class Reasonmaster(models.Model):
    reasonid = models.FloatField(db_column='ReasonId', blank=True, null=True)  # Field name made lowercase.
    reasonname = models.TextField(db_column='ReasonName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReasonMaster'


class Recipemain(models.Model):
    recipeid = models.FloatField(db_column='RecipeId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    totqty = models.FloatField(db_column='TotQty', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecipeMain'


class Recipesub(models.Model):
    recipeid = models.FloatField(db_column='RecipeId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecipeSub'


class Restrictionpswd(models.Model):
    pswd = models.TextField(db_column='Pswd', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestrictionPswd'


class Saledatemaster(models.Model):
    saleid = models.FloatField(db_column='SaleId', blank=True, null=True)  # Field name made lowercase.
    saledate = models.DateTimeField(db_column='SaleDate', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    t1000dhs = models.FloatField(db_column='t1000Dhs', blank=True, null=True)  # Field name made lowercase.
    t500dhs = models.FloatField(db_column='t500Dhs', blank=True, null=True)  # Field name made lowercase.
    t200dhs = models.FloatField(db_column='t200Dhs', blank=True, null=True)  # Field name made lowercase.
    t100dhs = models.FloatField(db_column='t100Dhs', blank=True, null=True)  # Field name made lowercase.
    t50dhs = models.FloatField(db_column='t50Dhs', blank=True, null=True)  # Field name made lowercase.
    t20dhs = models.FloatField(db_column='t20Dhs', blank=True, null=True)  # Field name made lowercase.
    t10dhs = models.FloatField(db_column='t10Dhs', blank=True, null=True)  # Field name made lowercase.
    t5dhs = models.FloatField(db_column='t5Dhs', blank=True, null=True)  # Field name made lowercase.
    t1dhs = models.FloatField(db_column='t1Dhs', blank=True, null=True)  # Field name made lowercase.
    t50fls = models.FloatField(db_column='t50Fls', blank=True, null=True)  # Field name made lowercase.
    t25fls = models.FloatField(db_column='T25Fls', blank=True, null=True)  # Field name made lowercase.
    totphysicalamt = models.FloatField(db_column='TotPhysicalAmt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaleDateMaster'


class Shiftmaster(models.Model):
    shiftid = models.FloatField(db_column='ShiftId', blank=True, null=True)  # Field name made lowercase.
    logindate = models.DateTimeField(db_column='LogInDate', blank=True, null=True)  # Field name made lowercase.
    logintime = models.CharField(db_column='LogInTime', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    logoutdate = models.DateTimeField(db_column='LogOutDate', blank=True, null=True)  # Field name made lowercase.
    logouttime = models.CharField(db_column='LogOutTime', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userid = models.FloatField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(db_column='UserName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saleid = models.FloatField(db_column='SaleId', blank=True, null=True)  # Field name made lowercase.
    saledate = models.DateTimeField(db_column='SaleDate', blank=True, null=True)  # Field name made lowercase.
    counterid = models.FloatField(db_column='CounterId', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    t1000dhs = models.FloatField(db_column='t1000Dhs', blank=True, null=True)  # Field name made lowercase.
    t500dhs = models.FloatField(db_column='t500Dhs', blank=True, null=True)  # Field name made lowercase.
    t200dhs = models.FloatField(db_column='t200Dhs', blank=True, null=True)  # Field name made lowercase.
    t100dhs = models.FloatField(db_column='t100Dhs', blank=True, null=True)  # Field name made lowercase.
    t50dhs = models.FloatField(db_column='t50Dhs', blank=True, null=True)  # Field name made lowercase.
    t20dhs = models.FloatField(db_column='t20Dhs', blank=True, null=True)  # Field name made lowercase.
    t10dhs = models.FloatField(db_column='t10Dhs', blank=True, null=True)  # Field name made lowercase.
    t5dhs = models.FloatField(db_column='t5Dhs', blank=True, null=True)  # Field name made lowercase.
    t1dhs = models.FloatField(db_column='t1Dhs', blank=True, null=True)  # Field name made lowercase.
    t50fls = models.FloatField(db_column='t50Fls', blank=True, null=True)  # Field name made lowercase.
    t25fls = models.FloatField(db_column='t25Fls', blank=True, null=True)  # Field name made lowercase.
    totphysicalamt = models.FloatField(db_column='TotPhysicalAmt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShiftMaster'


class Shrinkagemain(models.Model):
    refid = models.FloatField(db_column='RefId', blank=True, null=True)  # Field name made lowercase.
    refid1 = models.CharField(db_column='RefId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(db_column='RefDate', blank=True, null=True)  # Field name made lowercase.
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    duscant = models.FloatField(db_column='DuscAnt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vatamt = models.FloatField(db_column='VatAmt', blank=True, null=True)  # Field name made lowercase.
    grandtotal = models.FloatField(db_column='GrandTotal', blank=True, null=True)  # Field name made lowercase.
    trn = models.CharField(db_column='TRN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vatstatus = models.FloatField(db_column='VatStatus', blank=True, null=True)  # Field name made lowercase.
    reftype = models.FloatField(db_column='RefType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShrinkageMain'


class Shrinkagesub(models.Model):
    refid = models.FloatField(db_column='RefId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.FloatField(db_column='SellingPrice', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShrinkageSub'


class Sizemaster(models.Model):
    sizeid = models.FloatField(db_column='SizeId', blank=True, null=True)  # Field name made lowercase.
    sizename = models.TextField(db_column='SizeName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SizeMaster'


class Softday(models.Model):
    softdate = models.DateTimeField(db_column='SoftDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SoftDay'


class Softkeys(models.Model):
    id = models.FloatField(db_column='Id', blank=True, primary_key=True)  # Field name made lowercase.
    slno = models.CharField(db_column='SlNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    days = models.FloatField(db_column='Days', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SoftKeys'


class Softservice(models.Model):
    softstatus = models.FloatField(db_column='SoftStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SoftService'


class Staffdaytrans(models.Model):
    saledate = models.DateTimeField(db_column='SaleDate', blank=True, null=True)  # Field name made lowercase.
    staffid = models.FloatField(db_column='StaffId', blank=True, null=True)  # Field name made lowercase.
    delamt = models.FloatField(db_column='DelAmt', blank=True, null=True)  # Field name made lowercase.
    odelamt = models.FloatField(db_column='ODelAmt', blank=True, null=True)  # Field name made lowercase.
    tdelamt = models.FloatField(db_column='TDelAmt', blank=True, null=True)  # Field name made lowercase.
    bills = models.FloatField(db_column='Bills', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffDayTrans'


class Stockcard(models.Model):
    transid = models.FloatField(db_column='TransId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    refno = models.FloatField(db_column='RefNo', blank=True, null=True)  # Field name made lowercase.
    refno1 = models.CharField(db_column='RefNo1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(db_column='RefDate', blank=True, null=True)  # Field name made lowercase.
    reftype = models.CharField(db_column='RefType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qtyin = models.FloatField(db_column='QtyIn', blank=True, null=True)  # Field name made lowercase.
    qtyout = models.FloatField(db_column='QtyOut', blank=True, null=True)  # Field name made lowercase.
    costprice = models.FloatField(db_column='CostPrice', blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.FloatField(db_column='SellingPrice', blank=True, null=True)  # Field name made lowercase.
    locid = models.FloatField(db_column='LocId', blank=True, null=True)  # Field name made lowercase.
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockCard'


class Stockinmain(models.Model):
    stockinid = models.FloatField(db_column='StockInId', blank=True, null=True)  # Field name made lowercase.
    stockinid1 = models.CharField(db_column='StockInId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    indate = models.DateTimeField(db_column='InDate', blank=True, null=True)  # Field name made lowercase.
    fromlocid = models.FloatField(db_column='FromLocId', blank=True, null=True)  # Field name made lowercase.
    tolocid = models.FloatField(db_column='ToLocId', blank=True, null=True)  # Field name made lowercase.
    inamt = models.FloatField(db_column='InAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockInMain'


class Stockinsub(models.Model):
    stockinid = models.FloatField(db_column='StockInId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.FloatField(db_column='SellingPrice', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockInSub'


class Stockoutmain(models.Model):
    stockoutid = models.FloatField(db_column='StockOutId', blank=True, null=True)  # Field name made lowercase.
    stockoutid1 = models.CharField(db_column='StockOutId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    outdate = models.DateTimeField(db_column='OutDate', blank=True, null=True)  # Field name made lowercase.
    fromlocid = models.FloatField(db_column='FromLocId', blank=True, null=True)  # Field name made lowercase.
    tolocid = models.FloatField(db_column='ToLocId', blank=True, null=True)  # Field name made lowercase.
    outamt = models.FloatField(db_column='OutAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockOutMain'


class Stockoutsub(models.Model):
    stockoutid = models.FloatField(db_column='StockOutId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.FloatField(db_column='SellingPrice', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockOutSub'


class Subgroupmaster(models.Model):
    subgroupid = models.FloatField(db_column='SubGroupId', blank=True, primary_key=True)  # Field name made lowercase.
    groupid = models.FloatField(db_column='GroupId', blank=True, null=True)  # Field name made lowercase.
    subgroupname = models.TextField(db_column='SubGroupName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    groupstatus = models.CharField(db_column='GroupStatus', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    arabicname = models.TextField(db_column='ArabicName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubGroupMaster'


class Subgroupmaster2(models.Model):
    subgroupid = models.FloatField(db_column='SubGroupId', blank=True, null=True)  # Field name made lowercase.
    subgroupname = models.TextField(db_column='SubGroupName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubGroupMaster2'


class Subgroupmaster3(models.Model):
    subgroupid = models.FloatField(db_column='SubGroupId', blank=True, null=True)  # Field name made lowercase.
    subgroupname = models.TextField(db_column='SubGroupName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubGroupMaster3'


class Suppliermaster(models.Model):
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    suppname = models.TextField(db_column='SuppName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    add1 = models.TextField(db_column='Add1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    add2 = models.TextField(db_column='Add2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    add3 = models.TextField(db_column='Add3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telephoneno = models.CharField(db_column='TelephoneNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    faxno = models.CharField(db_column='FaxNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailid = models.TextField(db_column='EmailId', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    crdate = models.DateTimeField(db_column='CrDate', blank=True, null=True)  # Field name made lowercase.
    crid = models.FloatField(db_column='CrId', blank=True, null=True)  # Field name made lowercase.
    trn = models.CharField(db_column='TRN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SupplierMaster'


class Suppliersettlemain(models.Model):
    refno = models.FloatField(db_column='RefNo', blank=True, null=True)  # Field name made lowercase.
    refno1 = models.CharField(db_column='RefNo1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(db_column='RefDate', blank=True, null=True)  # Field name made lowercase.
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    settleamount = models.FloatField(db_column='SettleAmount', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    crdate = models.DateTimeField(db_column='CrDate', blank=True, null=True)  # Field name made lowercase.
    crid = models.FloatField(db_column='CrId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SupplierSettleMain'


class Suppliersettlesub(models.Model):
    refno = models.FloatField(db_column='RefNo', blank=True, null=True)  # Field name made lowercase.
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    invid1 = models.CharField(db_column='InvId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    invamt = models.FloatField(db_column='InvAmt', blank=True, null=True)  # Field name made lowercase.
    paidamt = models.FloatField(db_column='PaidAmt', blank=True, null=True)  # Field name made lowercase.
    balamt = models.FloatField(db_column='BalAmt', blank=True, null=True)  # Field name made lowercase.
    recamt = models.FloatField(db_column='RecAmt', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.
    cardamt = models.FloatField(db_column='CardAmt', blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.FloatField(db_column='DeliveryStatus', blank=True, null=True)  # Field name made lowercase.
    cardid = models.FloatField(db_column='CardId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SupplierSettleSub'


class Suppliertrans(models.Model):
    transid = models.FloatField(db_column='TransId', blank=True, null=True)  # Field name made lowercase.
    refid = models.FloatField(db_column='RefId', blank=True, null=True)  # Field name made lowercase.
    refid1 = models.CharField(db_column='RefId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(db_column='RefDate', blank=True, null=True)  # Field name made lowercase.
    custid = models.FloatField(db_column='CustId', blank=True, null=True)  # Field name made lowercase.
    creditamt = models.FloatField(db_column='CreditAmt', blank=True, null=True)  # Field name made lowercase.
    debitamt = models.FloatField(db_column='DebitAmt', blank=True, null=True)  # Field name made lowercase.
    transtype = models.CharField(db_column='TransType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    debitamtcard = models.FloatField(db_column='DebitAmtCard', blank=True, null=True)  # Field name made lowercase.
    cid = models.FloatField(db_column='CId', blank=True, null=True)  # Field name made lowercase.
    debitcashamt = models.FloatField(db_column='DebitCashAmt', blank=True, null=True)  # Field name made lowercase.
    debitbankamt = models.FloatField(db_column='DebitBankAmt', blank=True, null=True)  # Field name made lowercase.
    debitchequeamt = models.FloatField(db_column='DebitChequeAmt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SupplierTrans'


class Tablocationmaster(models.Model):
    id = models.FloatField(db_column='Id', blank=True, primary_key=True)  # Field name made lowercase.
    tab_type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    img_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tab_flag = models.IntegerField(blank=True, null=True)
    tablocation = models.FloatField(db_column='tabLocation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TabLocationMaster'


class Tablocationsection(models.Model):
    id = models.FloatField(db_column='Id', blank=True, primary_key=True)  # Field name made lowercase.
    location_section = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabLocationSection'


class Tabmaster(models.Model):
    id = models.FloatField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tabid = models.IntegerField(db_column='tabId', blank=True, null=True)  # Field name made lowercase.
    tabunique = models.CharField(db_column='tabUnique', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invseries = models.FloatField(db_column='InvSeries', blank=True, null=True)  # Field name made lowercase.
    invmaxno = models.FloatField(db_column='InvMaxNo', blank=True, null=True)  # Field name made lowercase.
    sectionid = models.FloatField(db_column='sectionId', blank=True, null=True)  # Field name made lowercase.
    location = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabMaster'


class Tabsectionmaster(models.Model):
    id = models.FloatField(db_column='Id', blank=True, primary_key=True)  # Field name made lowercase.
    tab_section = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabSectionMaster'


class Tablemaster(models.Model):
    tableid = models.FloatField(db_column='TableId', blank=True, primary_key=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sectionid = models.FloatField(db_column='SectionId', blank=True, null=True)  # Field name made lowercase.
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    invtime = models.CharField(db_column='InvTime', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invamt = models.FloatField(db_column='InvAmt', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    printstatus = models.FloatField(db_column='PrintStatus', blank=True, null=True)  # Field name made lowercase.
    addon = models.FloatField(db_column='AddOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TableMaster'


class Table1(models.Model):
    trn = models.CharField(db_column='TRN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    arabicname = models.CharField(db_column='ArabicName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_1'


class Tempkithcenprint(models.Model):
    invid = models.IntegerField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    korderno = models.IntegerField(db_column='KOrderNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempKithcenPrint'


class Tempprintinvoice(models.Model):
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    korderno = models.FloatField(db_column='KOrderNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempPrintInvoice'


class Toemailidsetting(models.Model):
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.
    emailid = models.TextField(db_column='EmailId', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ToEmailIdSetting'


class Tomailmaster(models.Model):
    toid = models.FloatField(db_column='ToId', blank=True, null=True)  # Field name made lowercase.
    tomailid = models.TextField(db_column='ToMailId', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ToMailMaster'


class Transcount(models.Model):
    transin = models.FloatField(db_column='TransIn', blank=True, null=True)  # Field name made lowercase.
    transout = models.FloatField(db_column='TransOut', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransCount'


class Transmain(models.Model):
    location_code = models.CharField(db_column='LOCATION_CODE', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    terminal_id = models.CharField(db_column='TERMINAL_ID', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shift_no = models.CharField(db_column='SHIFT_NO', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rcpt_num = models.FloatField(db_column='RCPT_NUM', blank=True, null=True)  # Field name made lowercase.
    rcpt_dt = models.DateTimeField(db_column='RCPT_DT', blank=True, null=True)  # Field name made lowercase.
    business_dt = models.DateTimeField(db_column='BUSINESS_DT', blank=True, null=True)  # Field name made lowercase.
    rcpt_tm = models.CharField(db_column='RCPT_TM', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inv_amt = models.FloatField(db_column='INV_AMT', blank=True, null=True)  # Field name made lowercase.
    tax_amt = models.FloatField(db_column='TAX_AMT', blank=True, null=True)  # Field name made lowercase.
    ret_amt = models.FloatField(db_column='RET_AMT', blank=True, null=True)  # Field name made lowercase.
    disc_amt = models.FloatField(db_column='DISC_AMT', blank=True, null=True)  # Field name made lowercase.
    op_cur = models.CharField(db_column='OP_CUR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bc_exch = models.FloatField(db_column='BC_EXCH', blank=True, null=True)  # Field name made lowercase.
    tran_status = models.CharField(db_column='TRAN_STATUS', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransMain'


class Transsub(models.Model):
    rcpt_dt = models.DateTimeField(db_column='RCPT_DT', blank=True, null=True)  # Field name made lowercase.
    rcpt_num = models.FloatField(db_column='RCPT_NUM', blank=True, null=True)  # Field name made lowercase.
    item_code = models.FloatField(db_column='ITEM_CODE', blank=True, null=True)  # Field name made lowercase.
    item_name = models.TextField(db_column='ITEM_NAME', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    item_qty = models.FloatField(db_column='ITEM_QTY', blank=True, null=True)  # Field name made lowercase.
    item_price = models.FloatField(db_column='ITEM_PRICE', blank=True, null=True)  # Field name made lowercase.
    item_cat = models.TextField(db_column='ITEM_CAT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    item_tax = models.FloatField(db_column='ITEM_TAX', blank=True, null=True)  # Field name made lowercase.
    item_tax_type = models.CharField(db_column='ITEM_TAX_TYPE', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    item_net_amt = models.FloatField(db_column='ITEM_NET_AMT', blank=True, null=True)  # Field name made lowercase.
    item_disc_amt = models.FloatField(db_column='ITEM_DISC_AMT', blank=True, null=True)  # Field name made lowercase.
    op_cur = models.CharField(db_column='OP_CUR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bc_exch = models.CharField(db_column='BC_EXCH', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    item_status = models.CharField(db_column='ITEM_STATUS', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransSub'


class Typemaster(models.Model):
    typeid = models.FloatField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    typename = models.TextField(db_column='TypeName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    typecode = models.CharField(db_column='TypeCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    exgrate = models.FloatField(db_column='ExgRate', blank=True, null=True)  # Field name made lowercase.
    typestatus = models.FloatField(db_column='TypeStatus', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeMaster'


class Typetrans(models.Model):
    typeid = models.FloatField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    invno = models.FloatField(db_column='InvNo', blank=True, null=True)  # Field name made lowercase.
    saleid = models.FloatField(db_column='SaleId', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    dhsamt = models.FloatField(db_column='DHSAmt', blank=True, null=True)  # Field name made lowercase.
    postingstatus = models.FloatField(db_column='PostingStatus', blank=True, null=True)  # Field name made lowercase.
    shiftid = models.FloatField(db_column='ShiftId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeTrans'


class Unitmaster(models.Model):
    unitid = models.FloatField(db_column='UnitId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnitMaster'


class Usermaster(models.Model):
    userid = models.FloatField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(db_column='UserName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userpswd = models.CharField(db_column='UserPswd', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usertype = models.FloatField(db_column='UserType', blank=True, null=True)  # Field name made lowercase.
    adminstatus = models.FloatField(db_column='AdminStatus', blank=True, null=True)  # Field name made lowercase.
    printername = models.CharField(db_column='PrinterName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserMaster'


class Userrights(models.Model):
    userid = models.FloatField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    modulecode = models.FloatField(db_column='ModuleCode', blank=True, null=True)  # Field name made lowercase.
    openrights = models.FloatField(db_column='OpenRights', blank=True, null=True)  # Field name made lowercase.
    newrights = models.FloatField(db_column='NewRights', blank=True, null=True)  # Field name made lowercase.
    editrights = models.FloatField(db_column='EditRights', blank=True, null=True)  # Field name made lowercase.
    saverights = models.FloatField(db_column='SaveRights', blank=True, null=True)  # Field name made lowercase.
    viewrights = models.FloatField(db_column='ViewRights', blank=True, null=True)  # Field name made lowercase.
    printrights = models.FloatField(db_column='PrintRights', blank=True, null=True)  # Field name made lowercase.
    deleterights = models.FloatField(db_column='DeleteRights', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserRights'


class Vatstatus(models.Model):
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VATStatus'


class Vatmaster(models.Model):
    vatid = models.FloatField(db_column='VatId', blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.FloatField(db_column='VATPercentage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VatMaster'


class Vatregistration(models.Model):
    trn = models.CharField(db_column='TRN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    arabicname = models.CharField(db_column='ArabicName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VatRegistration'


class Vouchermaster(models.Model):
    vouchid = models.FloatField(db_column='VouchId', blank=True, null=True)  # Field name made lowercase.
    vouchname = models.TextField(db_column='VouchName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VoucherMaster'


class PosCalls(models.Model):
    idnumber = models.IntegerField(db_column='IDNumber', blank=True, null=True)  # Field name made lowercase.
    linenumber = models.IntegerField(db_column='LineNumber', blank=True, null=True)  # Field name made lowercase.
    totalnumber = models.FloatField(db_column='TotalNumber', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(blank=True, null=True)
    custid = models.IntegerField(db_column='CustId', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    calldate = models.DateTimeField(db_column='CallDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pos_Calls'


class Repcollectionreport(models.Model):
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    invid1 = models.CharField(db_column='InvId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    totamt = models.FloatField(db_column='TotAmt', blank=True, null=True)  # Field name made lowercase.
    itemdiscamt = models.FloatField(db_column='ItemDiscAmt', blank=True, null=True)  # Field name made lowercase.
    invdiscamt = models.FloatField(db_column='InvDiscAmt', blank=True, null=True)  # Field name made lowercase.
    insuamt = models.FloatField(db_column='InsuAmt', blank=True, null=True)  # Field name made lowercase.
    vouchamt = models.FloatField(db_column='VouchAmt', blank=True, null=True)  # Field name made lowercase.
    cashadvamt = models.FloatField(db_column='CashAdvAmt', blank=True, null=True)  # Field name made lowercase.
    crcardadvamt = models.FloatField(db_column='CrCardAdvAmt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    cashamt = models.FloatField(db_column='CashAmt', blank=True, null=True)  # Field name made lowercase.
    crcardamt = models.FloatField(db_column='CrCardAmt', blank=True, null=True)  # Field name made lowercase.
    type = models.FloatField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'repCollectionReport'


class Repcustomerledger(models.Model):
    refno = models.FloatField(db_column='RefNo', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(db_column='RefDate', blank=True, null=True)  # Field name made lowercase.
    reftype = models.CharField(db_column='RefType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    creditamt = models.FloatField(db_column='CreditAmt', blank=True, null=True)  # Field name made lowercase.
    debitamt = models.FloatField(db_column='DebitAmt', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.
    custid = models.FloatField(db_column='CustId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'repCustomerLedger'


class Reppaymentreport(models.Model):
    paymentmode = models.TextField(db_column='PaymentMode', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'repPaymentReport'


class Repsupplierledger(models.Model):
    refno = models.FloatField(db_column='RefNo', blank=True, null=True)  # Field name made lowercase.
    refdate = models.DateTimeField(db_column='RefDate', blank=True, null=True)  # Field name made lowercase.
    reftype = models.CharField(db_column='RefType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    creditamt = models.FloatField(db_column='CreditAmt', blank=True, null=True)  # Field name made lowercase.
    debitamt = models.FloatField(db_column='DebitAmt', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.
    suppid = models.FloatField(db_column='SuppId', blank=True, null=True)  # Field name made lowercase.
    debitamtbank = models.FloatField(db_column='DebitAmtBank', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'repSupplierLedger'


class Tblheaderexport(models.Model):
    salesamt = models.FloatField(db_column='SalesAmt', blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHeaderExport'


class Tbllineexport(models.Model):
    docdate = models.DateTimeField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLineExport'


class Tbltransheaderexport(models.Model):
    salesamt = models.FloatField(db_column='SalesAmt', blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.
    docno = models.FloatField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTransHeaderExport'


class Tbltranslineexport(models.Model):
    docdate = models.DateTimeField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    docno = models.FloatField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    locname = models.TextField(db_column='LocName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTransLineExport'


class Tmpcreditsettlement(models.Model):
    invid1 = models.CharField(db_column='InvId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    invamt = models.FloatField(db_column='InvAmt', blank=True, null=True)  # Field name made lowercase.
    paidamt = models.FloatField(db_column='PaidAmt', blank=True, null=True)  # Field name made lowercase.
    balamt = models.FloatField(db_column='BalAmt', blank=True, null=True)  # Field name made lowercase.
    recamt = models.FloatField(db_column='RecAmt', blank=True, null=True)  # Field name made lowercase.
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.
    refno = models.FloatField(db_column='RefNo', blank=True, null=True)  # Field name made lowercase.
    pdcreamt = models.FloatField(db_column='pdCreAmt', blank=True, null=True)  # Field name made lowercase.
    cramt = models.FloatField(db_column='CrAmt', blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.CharField(db_column='DeliveryStatus', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpCreditSettlement'


class Tmpitem(models.Model):
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpItem'


class Tmpitemid(models.Model):
    itemid = models.FloatField(db_column='ItemID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpItemId'


class Tmpitems(models.Model):
    itemid1 = models.CharField(db_column='ItemId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpItems'


class Tmponlinedayreport(models.Model):
    saleid = models.FloatField(db_column='SaleId', blank=True, null=True)  # Field name made lowercase.
    onlineid = models.FloatField(db_column='OnlineId', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    shiftid = models.FloatField(db_column='ShiftId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpOnlineDayReport'


class Tmpphysicalstock(models.Model):
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    itemid1 = models.CharField(db_column='ItemId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemname = models.TextField(db_column='ItemName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    compqty = models.FloatField(db_column='CompQty', blank=True, null=True)  # Field name made lowercase.
    phyqty = models.FloatField(db_column='PhyQty', blank=True, null=True)  # Field name made lowercase.
    diffqty = models.FloatField(db_column='DiffQty', blank=True, null=True)  # Field name made lowercase.
    addqty = models.FloatField(db_column='AddQty', blank=True, null=True)  # Field name made lowercase.
    redqty = models.FloatField(db_column='RedQty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpPhysicalStock'


class Tmppurchaseitems(models.Model):
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    itemid1 = models.CharField(db_column='ItemId1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemname = models.TextField(db_column='ItemName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    costprice = models.FloatField(db_column='CostPrice', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.FloatField(db_column='SellingPrice', blank=True, null=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpPurchaseItems'


class Tmprunningtable(models.Model):
    tableid = models.FloatField(db_column='TableId', blank=True, null=True)  # Field name made lowercase.
    tablename = models.TextField(db_column='TableName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sectionid = models.FloatField(db_column='SectionId', blank=True, null=True)  # Field name made lowercase.
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    invtime = models.TextField(db_column='InvTime', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    invamt = models.FloatField(db_column='InvAmt', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.FloatField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    printstatus = models.FloatField(db_column='PrintStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpRunningTable'


class Tmpsplititems(models.Model):
    invid = models.FloatField(db_column='InvId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.FloatField(db_column='ItemId', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    totamt = models.FloatField(db_column='TotAmt', blank=True, null=True)  # Field name made lowercase.
    discamt = models.FloatField(db_column='DiscAmt', blank=True, null=True)  # Field name made lowercase.
    netamt = models.FloatField(db_column='NetAmt', blank=True, null=True)  # Field name made lowercase.
    costprice = models.FloatField(db_column='CostPrice', blank=True, null=True)  # Field name made lowercase.
    slno = models.FloatField(db_column='SlNo')  # Field name made lowercase.
    docno = models.FloatField(db_column='DocNo', blank=True, null=True)  # Field name made lowercase.
    locname = models.TextField(db_column='LocName', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    korderno = models.FloatField(db_column='KOrderNo', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    kitchenid = models.FloatField(db_column='KitchenId', blank=True, null=True)  # Field name made lowercase.
    kotnotes = models.CharField(db_column='KOTNotes', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpSplitItems'


class Tmptype(models.Model):
    typeid = models.FloatField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    damt = models.FloatField(db_column='DAmt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpType'


class Tmptypedayreport(models.Model):
    saleid = models.FloatField(db_column='SaleId', blank=True, null=True)  # Field name made lowercase.
    typeid = models.FloatField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    amt = models.FloatField(db_column='Amt', blank=True, null=True)  # Field name made lowercase.
    damt = models.FloatField(db_column='DAmt', blank=True, null=True)  # Field name made lowercase.
    shiftid = models.FloatField(db_column='ShiftId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpTypeDayReport'
