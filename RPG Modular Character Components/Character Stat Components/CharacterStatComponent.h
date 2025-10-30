// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "CharacterStatBase.h"
#include "CharacterStatComponent.generated.h"

/**
 * 
 */
UCLASS(ClassGroup = (Custom), meta = (BlueprintSpawnableComponent))
class MODULARCHARSTATS_API UCharacterStatComponent : public UCharacterStatBase
{
	GENERATED_BODY()
public: 
	UCharacterStatComponent();

	float GetPercent(CharStatName name);
	int Set(float current, float max, float regenRate, CharStatName name);
	int Adjust(float amount, CharStatName name);

protected:
	// Called when the game starts
	virtual void BeginPlay() override;

	// Called every frame
	virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

private:
	void PassiveAdjustment();

protected:
	UCharacterStatBase* Health;
	UCharacterStatBase* Stamina;
	UCharacterStatBase* Hunger;
	UCharacterStatBase* Thirst;
};
