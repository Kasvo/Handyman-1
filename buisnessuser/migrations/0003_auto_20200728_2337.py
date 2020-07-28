# Generated by Django 3.0.8 on 2020-07-28 18:07

import buisnessuser.models
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('buisnessuser', '0002_auto_20200726_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='professional_user',
            name='is_professional_user',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='professional_user',
            name='user_Img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='professional_user',
            name='Contact_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='professional_user',
            name='account_creation',
            field=buisnessuser.models.CustomDateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='professional_user',
            name='address',
            field=models.CharField(default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='professional_user',
            name='city',
            field=models.CharField(choices=[('AGRA', 'Agra'), ('AHMEDABAD', 'Ahmedabad'), ('ALAPPUZHA', 'Alappuzha'), ('ALWAR', 'Alwar'), ('AMRITSAR', 'Amritsar'), ('AURANGABAD', 'Aurangabad'), ('BANGALORE', 'Bangalore'), ('BHARATPUR', 'Bharatpur'), ('BHAVANAGAR', 'Bhavnagar'), ('BHIKANER', 'Bhikaner'), ('BHOPAL', 'Bhopal'), ('BHUBANESHWAR', 'Bhubaneshwar'), ('BODH GAYA', 'Bodh Gaya'), ('CALANGUTE', 'Calangute'), ('CHANDIGARH', 'Chandigarh'), ('CHENNAI', 'Chennai'), ('CHITTAURGARH', 'Chittaurgarh'), ('COIMBATHORE', 'Coimbatore'), ('CUTTACK', 'Cuttack'), ('DALHOUSIE', 'Dalhousie'), ('DEHRADUN', 'Dehradun'), ('DELHI', 'Delhi'), ('DIU_ISLAND', 'Diu - Island'), ('ERNAKULAM', 'Ernakulam'), ('FARIDABAD', 'Faridabad'), ('GAYA', 'Gaya'), ('GANGTOK', 'Gangtok'), ('GHAZIBAD', 'Ghaziabad'), ('GURGAON', 'Gurgaon'), ('GUWAHATI', 'Guwahati'), ('GWALIOR', 'Gwalior'), ('HARIDWAR', 'Haridwar'), ('HYDERABAD', 'Hyderabad'), ('IMPHAL', 'Imphal'), ('INDORE', 'Indore'), ('JBALPUR', 'Jabalpur'), ('JAIPUR', 'Jaipur'), ('JAISALMAR', 'Jaisalmer'), ('JALANDHAR', 'Jalandhar'), ('JAMSHEDPUR', 'Jamshedpur'), ('JODHPUR', 'Jodhpur'), ('JANAGARH', 'Junagadh'), ('KANPUR', 'Kanpur'), ('KANYAKUMARI', 'Kanyakumari'), ('KHAJURAHO', 'Khajuraho'), ('KHANDALA', 'Khandala'), ('KOCHI', 'Kochi'), ('KODAIKANAL', 'Kodaikanal'), ('KILKATA', 'kolkata'), ('KOTA', 'Kota'), ('KOTTAYAM', 'Kottayam'), ('KOVALAM', 'Kovalam'), ('LUCKNOW', 'Lucknow'), ('LUDHIANA', 'Ludhiana'), ('MADURAI', 'Madurai'), ('MANALI', 'Manali'), ('MANGALORE', 'Mangalore'), ('MARGAO', 'Margao'), ('MATHURA', 'Mathura'), ('MOUNRABU', 'Mountabu'), ('MUMBAI', 'Mumbai'), ('MUSSORIE', 'Mussoorie'), ('MYSORE', ' Mysore'), ('MANALI', 'Manali'), ('NAGPUR', 'Nagpur'), ('NAINITAL', 'Nainital'), ('NOIDA', 'Noida'), ('OOTY', 'Ooty'), ('ORCHHA', 'Orchha'), ('PANAJI', 'Panaji'), ('PATNA', 'Patna'), ('PONDICHERRY', 'Pondicherry'), ('PORBANDAR', 'Porbandar'), ('PORTBLAIR', 'Portblair'), ('PUNE', 'Pune'), ('PURI', 'Puri'), ('PUSHKAR', 'Pushkar'), ('RAJKOT', 'Rajkot'), ('RAMESHWARAM', 'Rameswaram'), ('RANCHI', 'Ranchi'), ('SANCHI', 'Sanchi'), ('SECUNDERABAD', 'Secunderabad'), ('SHIMLA', 'Shimla'), ('SURAT', 'Surat'), ('THAJAVUR', 'Thanjavur'), ('THIRUCHIRAPALLI', 'Thiruchchirapalli'), ('THRISSUR', 'Thrissur'), ('TIRUMALA', 'Tirumala'), ('UDAIPUR', 'Udaipur'), ('VADODRA', 'Vadodra'), ('VARANASI', 'Varanasi'), ('VASCO-DA-GAMA', 'Vasco - Da - Gama'), ('VIJAYAWADA', 'Vijayawada'), ('VISAKHAPATNAM', 'Visakhapatnam')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='professional_user',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='professional_user',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='professional_user',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='professional_user',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='professional_user',
            name='otp_gen_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='professional_user',
            name='token',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
