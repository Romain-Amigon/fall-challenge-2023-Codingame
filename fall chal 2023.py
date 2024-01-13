
def distance(X,Y):

    x,y=X
    x1,y1=Y
    return ( ( x-x1)**2+ (y-y1)**2)**0.5

def nombre(a):
    if a==0 or a==3:
        return 0
    else:
        return 1



class drone:

    def __init__(self,id,x,y,emergency,light,scan,radar):
        self.id=id
        self.x=x
        self.y=y
        self.emergency=emergency
        self.light=light
        self.scan=scan
        self.radar=radar
        

class fish :

    def __init__(self,x,y,vx,vy,color,typ,visible):
        
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.color=color
        self.typ=typ
        self.visible=visible

class scan:

    def __init__(self,save,scan):
        self.save=save
        self.scan=scan

creature_count = int(input())
Fish=[fish(0,0,0,0,0,0,0) for i in range(creature_count)]
for i in range(creature_count):
    creature_id, color, typ = [int(j) for j in input().split()]
    
    Fish[creature_id-4].color=color
    Fish[creature_id-4].typ=typ

Lpir=[[0 for i in range(creature_count-12)],[0 for i in range(creature_count-12)]]
light=0
while True:
    for i in Fish:
        i.visible=0

    my_score = int(input())
    foe_score = int(input())

    My_id_drones=[]
    my_scan = scan([],[])
    my_scan_count = int(input())
    for i in range(my_scan_count):
        creature_id = int(input())
        my_scan.save.append(creature_id)
        

    foe_scan=scan([],[])

    foe_scan_count = int(input())
    for i in range(foe_scan_count):
        creature_id = int(input())
        foe_scan.save.append(creature_id)

    
    My_drones=[]
    my_drone_count = int(input())
    for i in range(my_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]
        My_drones.append(drone(drone_id, drone_x, drone_y, emergency, light,[],[]))
        My_id_drones.append(drone_id)

    foe_drone_count = int(input())
    for i in range(foe_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]

    drone_scan_count = int(input())
    for i in range(drone_scan_count):
        drone_id, creature_id = [int(j) for j in input().split()]

        if drone_id in My_id_drones:
            if creature_id not in my_scan.scan:
                my_scan.scan.append(creature_id)
            for j in My_drones:
                if j.id==drone_id:
                    j.scan.append(creature_id)

    Visible=[]
    visible_creature_count = int(input())
    for i in range(visible_creature_count):
        creature_id, creature_x, creature_y, creature_vx, creature_vy = [int(j) for j in input().split()]
        Fish[creature_id-4].x=creature_x
        Fish[creature_id-4].y=creature_y
        Fish[creature_id-4].vx=creature_vx
        Fish[creature_id-4].vy=creature_vy
        
        if creature_x<=9999 and creature_x>=0 :
            
            Fish[creature_id-4].visible=1

            if creature_id<16 and creature_id not in my_scan.scan and creature_id not in my_scan.save:
                Visible.append(creature_id)
        


    radar_blip_count = int(input())
    for i in range(radar_blip_count):
        inputs = input().split()
        drone_id = int(inputs[0])
        creature_id = int(inputs[1])
        radar = inputs[2]

        for j in My_drones:
            if j.id==drone_id :
                if creature_id not in my_scan.scan and creature_id not in my_scan.save and creature_id<16:
                    j.radar.append((creature_id,radar))

    for i in My_drones:
        x,y=5000,5000
        prex=i.x
        prey=i.y
        
        
        Radar=i.radar
        
        light=0

        if prey>2900 and i.light==0:
            light=1
        i.light= light

        radar="TL"
        r=[]
        for j in Radar:
            if j[0] not in my_scan.scan and j[0] not in my_scan.save:
                r.append(j[1])
        if r!=[]:

            radar=r[-nombre(i.id)]
        
        for j in r :

            if nombre(i.id)==0:
                
                if j=="TL" or j=="BL":
                    radar=j
            if nombre(i.id)==1:
                if j=="TR" or j=="BR":
                    radar=j
        


        if len(Visible)==0:
            if radar =="TL":
                x,y=0,0
            if radar=="TR":
                x,y=9999,0
            if radar=="BL":
                x,y=0,9999
            if radar=="BR":
                x,y=9999,9999
        a=0
        for j in range(len(Fish)):
            if Fish[j].visible and j+4 not in my_scan.scan and j+4 not in my_scan.save and distance((prex,prey),(Fish[j].x,Fish[j].y))<1999 and Fish[j].typ!=-1:
                
                x,y=Fish[j].x,Fish[j].y
            
            


        if len(i.scan)>6 or len(Radar)==0:
            x=prex
            y=0

        if len(i.scan)>3 and prey<2500:
            x=prex
            y=0
        if len(i.scan)>0 and prey<1500:
            x=prex
            y=0
        if len(i.scan)>1 and prey<2000:
            x=prex
            y=0


        dmax=150000
        for j in range(len(Fish)):
            d=distance((prex,prey),(Fish[j].x,Fish[j].y))
            if Fish[j].visible and Fish[j].typ==-1 and d<2300:
                
                dmax=d
                x=int(x-1000*Fish[j].x/abs(d+0.1-1000))
                y=int(y-1000*Fish[j].y/abs(d+0.1-1000))
                a=1
                Lpir[nombre(i.id)][j-12]=1
            
            if not Fish[j].visible and Fish[j].typ==-1 and d<1500 and Lpir[nombre(i.id)][j-12]==1:
                x=(-Fish[j].x)
                y=(-Fish[j].y)
                a=1
                Lpir[nombre(i.id)][j-12]=0
            


        
        print("MOVE",x,y,light,dmax)
        
