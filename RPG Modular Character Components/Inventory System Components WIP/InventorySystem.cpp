// Fill out your copyright notice in the Description page of Project Settings.


#include "InventorySystem.h"

// Sets default values for this component's properties
UInventorySystem::UInventorySystem()
{
	// Set this component to be initialized when the game starts, and to be ticked every frame.  You can turn these features
	// off to improve performance if you don't need them.
	PrimaryComponentTick.bCanEverTick = false;
	maxInventorySize = 10;
	currentInventorySize = 0;
	currentWeight = 0.0f;
	maxWeight = 100.0f;
	totalCurrency = 0.0f;

}


// Called when the game starts
void UInventorySystem::BeginPlay()
{;
	
}

void UInventorySystem::Add(UWeaponItem* item)
{
	int index = -1;
	bool flag = false;
	UItemBase* pBase = (UItemBase*)item;
	flag = inventoryArray.Find(pBase, index);

	if (flag)
	{
		if (item->GetCurrentStackSize() + 1 <= item->GetMaxStackSize())
		{
			UItemBase* itemBase = inventoryArray[index];
			itemBase->AdjustStackSize(itemBase->GetCurrentStackSize() + 1);
		}
		else
		{
			inventoryArray.Emplace(item);
		}

	}
	else
	{
		inventoryArray.Emplace(item);
	}
	this->currentWeight += item->getWeight();
	this->currentInventorySize++;
}

void UInventorySystem::Add(UArmorItem* item)
{
	int index = -1;
	bool flag = false;
	UItemBase* pBase = (UItemBase*)item;
	flag = inventoryArray.Find(pBase, index);

	if (flag)
	{
		if (item->GetCurrentStackSize() + 1 <= item->GetMaxStackSize())
		{
			UItemBase* itemBase = inventoryArray[index];
			itemBase->AdjustStackSize(itemBase->GetCurrentStackSize() + 1);
		}
		else
		{
			inventoryArray.Emplace(item);
		}

	}
	else
	{
		inventoryArray.Emplace(item);
	}
	this->currentWeight += item->getWeight();
	this->currentInventorySize++;
}

void UInventorySystem::Add(UElixirItem* item)
{
	int index = -1;
	bool flag = false;
	UItemBase* pBase = (UItemBase*)item;
	flag = inventoryArray.Find(pBase, index);

	if (flag)
	{
		if (item->GetCurrentStackSize() + 1 <= item->GetMaxStackSize())
		{
			UItemBase* itemBase = inventoryArray[index];
			itemBase->AdjustStackSize(itemBase->GetCurrentStackSize() + 1);
		}
		else
		{
			inventoryArray.Emplace(item);
		}

	}
	else
	{
		inventoryArray.Emplace(item);
	}
	this->currentWeight += item->getWeight();
	this->currentInventorySize++;
}

void UInventorySystem::Add(UAmmunitionItem* item)
{
	int index = -1;
	bool flag = false;
	UItemBase* pBase = (UItemBase*)item;
	flag = inventoryArray.Find(pBase, index);

	if (flag)
	{
		if (item->GetCurrentStackSize() + 1 <= item->GetMaxStackSize())
		{
			UItemBase* itemBase = inventoryArray[index];
			itemBase->AdjustStackSize(itemBase->GetCurrentStackSize() + 1);
		}
		else
		{
			inventoryArray.Emplace(item);
		}

	}
	else
	{
		inventoryArray.Emplace(item);
	}
	this->currentWeight += item->getWeight();
	this->currentInventorySize++;
}

void UInventorySystem::Add(UFoodItem* item)
{
	int index = -1;
	bool flag = false;
	UItemBase* pBase = (UItemBase*)item;
	flag = inventoryArray.Find(pBase, index);

	if (flag)
	{
		if (item->GetCurrentStackSize() + 1 <= item->GetMaxStackSize())
		{
			UItemBase* itemBase = inventoryArray[index];
			itemBase->AdjustStackSize(itemBase->GetCurrentStackSize() + 1);
		}
		else
		{
			inventoryArray.Emplace(item);
		}

	}
	else
	{
		inventoryArray.Emplace(item);
	}
	this->currentWeight += item->getWeight();
	this->currentInventorySize++;
}

void UInventorySystem::Add(UCurrencyItem* item)
{
	this->totalCurrency += item->getCost();
}

void UInventorySystem::Add(UMiscItem* item)
{
	int index = -1;
	bool flag = false;
	UItemBase* pBase = (UItemBase*)item;
	flag = inventoryArray.Find(pBase, index);

	if (flag)
	{
		if (item->GetCurrentStackSize() + 1 <= item->GetMaxStackSize())
		{
			UItemBase* itemBase = inventoryArray[index];
			itemBase->AdjustStackSize(itemBase->GetCurrentStackSize() + 1);
		}
		else
		{
			inventoryArray.Emplace(item);
		}

	}
	else
	{
		inventoryArray.Emplace(item);
	}
	this->currentWeight += item->getWeight();
	this->currentInventorySize++;
}

void UInventorySystem::AddItem(UItemBase* item)
{
	int index = -1;
	bool flag = false;
	UItemBase* pBase = (UItemBase*)item;
	flag = inventoryArray.Find(pBase, index);

	if (flag)
	{
		if (item->GetCurrentStackSize() + 1 <= item->GetMaxStackSize())
		{
			UItemBase* itemBase = inventoryArray[index];
			itemBase->AdjustStackSize(itemBase->GetCurrentStackSize() + 1);
		}
		else
		{
			inventoryArray.Emplace(item);
		}

	}
	else
	{
		inventoryArray.Emplace(item);
	}
	this->currentWeight += item->getWeight();
	this->currentInventorySize++;
}

UItemBase* UInventorySystem::GetItem(FString itemName)
{
	UItemBase* pBase;
	for (int index = 0; index != inventoryArray.Num(); index++)
	{
		pBase = inventoryArray[index];
		if (pBase->GetName() == itemName)
		{
			return pBase;
		}
	}
	return nullptr;
}


//// Called every frame
//void UInventorySystem::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
//{
//	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);
//
//	// ...
//}
