import json
import csv
from datetime import datetime, timedelta
import io


def generate_ad(ad_content, platform, company_name):            #function takes in generated ad campaign data to display in form of platform ad structure using html
    if platform.lower() == "facebook":                          #different base structure for different platforms
        return f"""<!DOCTYPE html>
        <html>
        <head>
            <title>{ad_content.get('campaign_name', 'Facebook Ad Preview')}</title>
            <meta charset="UTF-8">
        </head>
        <body>
            <div style="border: 1px solid #dddfe2; border-radius: 8px; padding: 12px; margin-bottom: 16px; background-color: #f5f6f7;">
                <div style="font-weight: bold; color: black;">{company_name}</div>
                <div style="color: #606770; font-size: 12px;">Sponsored</div>
            </div>
            <div style="border: 1px solid #dddfe2; border-radius: 8px; padding: 12px; margin-bottom: 16px;">
                {ad_content.get('ad_copy', 'Ad copy goes here')}
            </div>
            <div style="border: 1px solid #dddfe2; border-radius: 8px; height: 250px; display: flex; align-items: center; justify-content: center; background-color: #f0f2f5; margin-bottom: 16px;">
                <p style="color: #65676b;">[Image would appear here]</p>                
            </div>
            <div style="border: 1px solid #dddfe2; border-radius: 8px; padding: 12px; background-color: #f5f6f7;">
                <div style="font-weight: bold; color:black; font-size: 18px;">{ad_content.get('headline', 'Headline')}</div>
                <div style="color: #606770; padding: 8px 0;">{ad_content.get('description', 'Description')}</div>
                <button style="background-color: #1877f2; color: white; border: none; border-radius: 6px; padding: 8px 12px; font-weight: bold; cursor: pointer; width: 100%;">{ad_content.get('cta', 'Learn More')}</button>
            </div>
        </body>
        </html>"""
    
    elif platform.lower() == "instagram":
        return f"""<!DOCTYPE html>
        <html>
        <head>
            <title>{ad_content.get('campaign_name', 'Instagram Ad Preview')}</title>
            <meta charset="UTF-8">
        </head>
        <body>
            <div style="border: 1px solid #dbdbdb; border-radius: 3px; padding: 14px 16px; margin-bottom: 16px; display: flex; align-items: center;">
                <div style="width: 32px; height: 32px; background-color: #dbdbdb; border-radius: 50%;"></div>
                <div style="margin-left: 14px;">
                    <div style="font-weight: 600;">{company_name}</div>
                    <div style="font-size: 12px; color: #8e8e8e;">Sponsored</div>
                </div>
            </div>
            <div style="border: 1px solid #dbdbdb; border-radius: 3px; height: 400px; display: flex; align-items: center; justify-content: center; background-color: #efefef; margin-bottom: 16px;">
                <p style="color: #8e8e8e;">[Image would appear here]</p>
            </div>
            <div style="border: 1px solid #dbdbdb; border-radius: 3px; padding: 12px 16px;">
                <div style="margin-bottom: 12px; line-height: 1.4;">{ad_content.get('ad_copy', 'Ad copy goes here')}</div>
                <div style="font-weight: 600; margin-bottom: 8px;">{ad_content.get('headline', 'Headline')}</div>
                <button style="background-color: #0095f6; color: white; border: none; border-radius: 4px; padding: 8px 12px; font-weight: 600; cursor: pointer; width: 100%;">{ad_content.get('cta', 'Learn More')}</button>
            </div>
        </body>
        </html>"""
    
    elif platform.lower() == "linkedin":
        return f"""<!DOCTYPE html>
        <html>
        <head>
            <title>{ad_content.get('campaign_name', 'Instagram Ad Preview')}</title>
            <meta charset="UTF-8">
        </head>
        <body>
            <div style="border: 1px solid #e0e0e0; padding: 12px; margin-bottom: 16px; display: flex; align-items: center;">
            <div style="width: 40px; height: 40px; background-color: #0a66c2; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">C</div>
            <div style="margin-left: 12px;">
                <div style="font-weight: 600;">{company_name}</div>
                <div style="font-size: 12px; color: #666666;">Sponsored · <span style="color: #0a66c2;">Follow</span></div>
            </div>
            </div>
            <div style="border: 1px solid #e0e0e0; padding: 16px; margin-bottom: 16px;">
                <div style="margin-bottom: 16px; line-height: 1.5;">{ad_content.get('ad_copy', 'Ad copy goes here')}</div>
            </div>
            <div style="border: 1px solid #e0e0e0; height: 290px; display: flex; align-items: center; justify-content: center; background-color: #f5f5f5; margin-bottom: 16px;">
                <p style="color: #666666;">[Image would appear here]</p>
            </div>
            <div style="border: 1px solid #e0e0e0; padding: 16px; background-color: #f9f9f9;">
                <div style="font-weight: 600; font-size: 16px; margin-bottom: 8px; color:black;">{ad_content.get('headline', 'Headline')}</div>
                <div style="color: #666666; margin-bottom: 16px;">{ad_content.get('description', 'Description')}</div>
                <button style="background-color: #0a66c2; color: white; border: none; border-radius: 16px; padding: 6px 16px; font-weight: 600; cursor: pointer;">{ad_content.get('cta', 'Learn More')}</button>
            </div>
        </body?
        </html>"""
    
    elif platform.lower() == "tiktok":
        return f"""<!DOCTYPE html>
        <html>
        <head>
            <title>{ad_content.get('campaign_name', 'Instagram Ad Preview')}</title>
            <meta charset="UTF-8">
        </head>
        <body>
            <div style="border: 1px solid #333; border-radius: 8px; background-color: #000; color: white; padding: 12px; margin-bottom: 16px; display: flex; align-items: center;">
            <div style="width: 40px; height: 40px; background-color: #EE1D52; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">C</div>
            <div style="margin-left: 12px;">
                <div style="font-weight: 600;">@{company_name}</div>
                <div style="font-size: 12px; color: #AAAAAA;">Sponsored</div>
            </div>
            </div>
            <div style="border: 1px solid #333; border-radius: 8px; height: 500px; background-color: #111; position: relative; margin-bottom: 16px;">
                <p style="color: #AAAAAA; text-align: center; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">[Video would appear here]</p>
                <div style="position: absolute; bottom: 20px; left: 12px; right: 12px;">
                    <div style="margin-bottom: 12px; line-height: 1.4;">{ad_content.get('ad_copy', 'Ad copy goes here')}</div>
                    <div style="font-weight: 600; margin-bottom: 8px;">{ad_content.get('headline', 'Headline')}</div>
                    <button style="background-color: #EE1D52; color: white; border: none; border-radius: 4px; padding: 8px 12px; font-weight: 600; cursor: pointer; width: 100%;">{ad_content.get('cta', 'Learn More')}</button>
                </div>
            </div>
        </body?
        </html>"""
        #option to add images and advertisements in the "Image" placeholder by placing urls (can be done via automated web scraping too)
def convert_to_csv(ad_content, platform):                                   #converting ad campaign data generated to csv format for downloading
    output = io.StringIO()
    writer = csv.writer(output)
    
    if platform.lower() in ["facebook", "instagram"]:
        writer.writerow(['Campaign Name', 'Ad Set Name', 'Ad Name', 'Objective',
                       'Daily Budget', 'Start Date', 'End Date', 'Headline',
                       'Description', 'Ad Text', 'Call To Action'])
        
        start_date = datetime.now().strftime("%Y-%m-%d")
        end_date = (datetime.now() + timedelta(days=int(ad_content.get('campaign_duration_days', 14)))).strftime("%Y-%m-%d")
        
        writer.writerow([
            ad_content.get('campaign_name', 'Campaign'),
            f"{ad_content.get('campaign_name', 'Campaign')} - Ad Set",
            f"{ad_content.get('campaign_name', 'Campaign')} - Ad",
            ad_content.get('objective', 'CONVERSIONS'),
            ad_content.get('suggested_budget_daily', 20),
            start_date,
            end_date,
            ad_content.get('headline', ''),
            ad_content.get('description', ''),
            ad_content.get('ad_copy', ''),
            ad_content.get('cta', 'LEARN_MORE')
        ])
    else:
        writer.writerow(['Field', 'Value'])
        for key, value in ad_content.items():
            if isinstance(value, (list, dict)):
                writer.writerow([key, json.dumps(value)])
            else:
                writer.writerow([key, value])
    
    return output.getvalue()
