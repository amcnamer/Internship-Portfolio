// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "WeaponItem.h"
#include "ArmorItem.h"
#include "ElixirItem.h"
#include "AmmunitionItem.h"
#include "FoodItem.h"
#include "CurrencyItem.h"
#include "MiscItem.h"
#include "InventorySystem.generated.h"

//USTRUCT(BlueprintType)
//struct FWeaponItem : public FItem
//{
//	GENERATED_USTRUCT_BODY();
//
//	FWeaponItem();
//	FWeaponItem(int stackSize, float weight, float currencyCost, ItemType type, int weaponDamage, ItemTier tier);
//
//	int weaponDamage = 0.0f;
//	ItemTier tier = ItemTier::UNINITIALIZED;
//};



UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class MODULARCHARSTATS_API UInventorySystem : public UActorComponent
{
	GENERATED_BODY()

public:	
	// Sets default values for this component's properties
	UInventorySystem();

protected:
	// Called when the game starts
	virtual void BeginPlay() override;

public:	
	// Called every frame
	//virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;
	void Add(UWeaponItem* item);
	void Add(UArmorItem* item);
	void Add(UElixirItem* item);
	void Add(UAmmunitionItem* item);
	void Add(UFoodItem* item);
	void Add(UCurrencyItem* item);
	void Add(UMiscItem* item);
	void AddItem(UItemBase* item);

	UItemBase* GetItem(FString itemName);

		

public:
	int maxInventorySize;
	int currentInventorySize;
	float currentWeight;
	float maxWeight;
	float totalCurrency;
	TArray<UItemBase*> inventoryArray;
};
